package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"net/url"
	"os"
	"os/exec"
	"strings"
	"time"
)

var (
	CF_SITEKEY = getEnv("CF_SITEKEY", `"><script>document.write("CF Turnstile is broken")</script><div "`)
	CF_SECRET  = getEnv("CF_SECRET", "Sunny's Secret")
)

func getEnv(key, fallback string) string {
	value, exists := os.LookupEnv(key)
	if !exists {
		value = fallback
	}
	return value
}

func escapeShellArg(arg string) string {
	return "'" + strings.Replace(arg, "'", "'\\''", -1) + "'"
}

func release(w http.ResponseWriter, r *http.Request) {
	http.ServeFile(w, r, "app")
}

func index(w http.ResponseWriter, r *http.Request) {
	if r.Method == http.MethodPost && r.RemoteAddr != "127.0.0.1" {
		captchaResponse := r.FormValue("cf-turnstile-response")
		if captchaResponse == "" {
			fmt.Fprint(w, "Bad CF Captcha")
			return
		}
		data := url.Values{"secret": {CF_SECRET}, "response": {captchaResponse}}
		resp, err := http.PostForm("https://challenges.cloudflare.com/turnstile/v0/siteverify", data)
		if err != nil {
			fmt.Fprint(w, err)
			return
		}
		body, _ := ioutil.ReadAll(resp.Body)
		if !strings.Contains(string(body), `"success":true`) {
			fmt.Fprint(w, "CF Captcha is broken")
			return
		}
		urlStr := r.FormValue("url")
		if !strings.Contains(urlStr, "https://secureapp.sunnylo.tk/") {
			fmt.Fprint(w, "Invalid URL")
			return
		}
		openURL, err := url.Parse(urlStr)
		if err != nil {
			fmt.Fprint(w, err)
			return
		}
		command := "/app " + escapeShellArg(openURL.String())
		fmt.Println(r.RemoteAddr + ": " + command)
		cmd := exec.Command("/bin/sh", "-c", command)
		cmd.Dir = "/tmp"
		cmd.Start()
		done := make(chan error, 1)
		go func() {
			done <- cmd.Wait()
		}()
		select {
		case <-time.After(10 * time.Second):
			if err := cmd.Process.Kill(); err != nil {
				fmt.Println("failed to kill process: ", err)
			}
		case err := <-done:
			if err != nil {
				fmt.Println("process finished with error = ", err)
			}
		}
		fmt.Fprintf(w, "<title>Secure App</title><code>%s</code><hr />Bot should have viewed your webpage?", command)
	} else {
		fmt.Fprint(w, `<html>
<head>
<title>Secure App</title>
<script src="https://challenges.cloudflare.com/turnstile/v0/api.js" async defer></script>
</head>
<body>
<h2>Secure App</h2>
<form method="post">
<p style="font-family:Courier New;background:#CCCCCC;font-size:16pt;padding:0.25em">
/app
<input style="font-family:Courier New;background:#CCCCCC;font-size:16pt;border:0;width:90%" name="url">
</p>
<div class="cf-turnstile" data-sitekey="`+CF_SITEKEY+`"></div>
<p><input type="submit"></p>
</form>
<p>Remarks: 
<ul>
<li><a href="/app">Download the App in here</a></li>
<li>Timeout in 10 seconds</li>
</ul>
</p>
</body>
</html>`)
	}
}

func main() {
	http.HandleFunc("/app", release)
	http.HandleFunc("/", index)
	http.ListenAndServe(":5000", nil)
}
