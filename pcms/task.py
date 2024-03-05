import random
from Crypto.Util.number import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import gmpy2
import os
import hashlib
def xor(a, b):
    return bytes([a[i%len(a)] ^ b[i%len(b)] for i in range(max(len(a), len(b)))])
flag = b'flag{xxxxxx}'
key1 = hashlib.md5(os.urandom(16)).hexdigest().encode()
key2 = hashlib.md5(os.urandom(16)).hexdigest().encode()
num1 = 5
p = int(gmpy2.next_prime(bytes_to_long(key1 + os.urandom(64))))
ms = [random.getrandbits(256) for _ in range(num1)]
qs = [getPrime(1024) for _ in range(num1)]
ns = [p * qs[_] + ms[_] for _ in range(num1)]

num2 = 37
x = bytes_to_long(key2 + os.urandom(32))
A = []
B = []
for i in range(num2):
    a = random.getrandbits(512)
    b = a * x % p
    gift = (2 ** 128 - 1) * 2 ** 400
    A.append(a)
    B.append((b & gift) >> 400)

iv = long_to_bytes(random.getrandbits(128))
key = xor(key1,key2)
aes = AES.new(key1,AES.MODE_CBC,iv)
enc = aes.encrypt(pad(flag,48))
print(f'ns = {ns}')
print(f'A = {A}')
print(f'B = {B}')
print(f'enc = {enc}')
# ns = [38630062416586710341458654419912504176237737247477839749085033080367529539859992076587411537805430366799412095876782912512744262957062106155418341531142309858429218208463637096843365217114990765965110566415965985105403996944993619708417839598461935470469097206342256014086162845948208599334925650727933097059538199199685364793545286980392966271769914201657672004082101110775504946586957241075964270454872257405872181588544468173017149763827540561921126826597515171761064800381983526515300315517818122598179574900255685121991744205071544970, 41522753602903133841910260331594875922287719226997542592715810409935551768308104573333760854332533376702631593490915962706512143045107096658851885513727202513616813054397657610854303071682604806070009002234312854968365250748142324994926715544722158698813288131533399544263105858513134170084625526223987620550110255872688155827773099232631041345207194483609514502522566888883736218471849075697433311580004701384847571029783514418685068903758509270527252444771313048094566344002411364378658592832008194309873599342916391769027015343562030852, 41542983120532762175372001624404625565366126179958909731196555044290633581761361918706298428954501507557598076910710787422049443564800530253137695341299743714514361560156305534490483794181933110893966453220306980682146624294992100948497284459992930850081254114996830645068636306625330524465991656430799359422407117440063911943625477783216502523414967017151717597372146324488526509879620785458016456593044828784565522423332830549325397893426472247197776412026158371655860380929692662547882654137064941217130915364306358205055760044763651406, 42853015443318352230776688785915441259875645365236808434164117288657978345098324019250085686482568413223085548506789311679316323466083886556772338612177680666217592255234589446979456714341877135596118517098603502394776049958587301113539552072352462301070489369653155854389890761241450743607560719433910573462283304103064437843063566946231984094581307498714742271881862348689297267558023093643893310002803310596286441071314219020032740336515363830250477649030557311461077069407775907176409762823453607196260454965048316567154365877848652918, 31152961872836435078296602982779340735140569916125711058616435902653202922218293684857125091648631460215120167354825278469413413558325850576700866199515219603448136082693185200558425103833947831228064760642508443585470729998592994719564254894176473779555436230174300038353978808432410463449170865897259181312953584408177790825688497584119467820716449210429423337019604137134889051973100340798405991782200038835066294194815913887924272593864934325496116821854183293510325217934617021428710898873475027666892706022106386340733691632884942848]
# A = [12789809461864875489953273982997537541385904671489556544122095227619591140533414669794423644619127980362623481580128258914287474542792728686579090501397390, 10463950513938701625808784986819665844287315724639315128677227520960105897990256530542006653611594269012930935073966767351788182657861624733138283749460454, 5253244650607533810967862436125419800679723144526973463211784033045021824966560017919956773745212139142517766154626849426827164032731516615725539069585525, 5644589184984504085855423002268477365020278981591337230721358313393863912025011466727192648804002734561676112555123877764178690726130713927642577324443238, 4231732567865883627242742552738439372803539125622706171540910152922080004603138662537022248675968288205781990968838888633816697065257733344028576518431020, 2483388920404524165854675814798022834892112957478917588986471421083048888193527751575039626887367465858751417977246719312923814782809309525841102293919541, 3252353812256192711411255830105475125944842449239880454539397067913664088094160819193268643401968970009466652179043139341471403913410402646923633696154454, 11575010486066232687430367040977113580882826853104996856464797182632266635060724100357205810604915010810884387573114266349621457564659060272935537811111850, 116107444921917032985259963199427176510900273385517435613848456370557161312731449337837406563733552524777525870560544042690403987311424820755256727586807, 5859050133610438843641532306693688255014116940390205022708310454673159702673207152462501010791971695002865650407033762568636006764435795015869726867643634, 5954075553161305677556950650395792531753502207483036473422070018485916621872566706504374038792527687442272405589975343003802956899043321092006127828986114, 4571747544457157571652286537158051402285727327066029382085461714597609990601683125994983291866807816649968826930652068427193317966970789937746419206862747, 7166507561570980603812241332170524724051295937096000768984168029904561160020043035660087151672164814332446644696618077835020463308343415953131944864257266, 4852042788460566411381271873349329096978244586097817622748766708426751073559942708861852208085367014057217116211249133109246735634468823924185525972777655, 11962941918999276757181090570698839032103646409734781047194175833198626142790676141060052011581957980660140931408560130449153056874213033784715711461403345, 10324508881746579337486319574059121005227580732153432145860775835052420139026016902518605634385512021513380467928195663920843022679549517463264144660593354, 13276257094435850052122403884510025189232513948002582716865201271569293297601525601586036713056700716929820641888489806178376555435219630186396004003438962, 6525051273399089095687950615197786094425890004112675057642687348101531212837185750558500720306108976630502328600886080197626115513445112562084719104488315, 12922888505610354933000354792496863801007995464403098763485264334670452387681468617068312646367483171083114539083453125614861357751571161533921864394641576, 9489726784141062031514945333087338495823600723655465328127755755022980083351477888038160719541864899912899592065620071698977397662002448273876711116012763, 10630316198843195148937849513165933809121991192035364160395429088101265852052098101114542104327663563661384303617672183366879116750889320604308038959012109, 12675564142993964272844760955973914547747654087592111324261755301551267959231076883765863344473167582531968290671984039948163579495803204811731286282708940, 11847724105274460405216443356582445218232627275228120716891711887600046501095390733716854871561352002320819466803698088448952127166615410820121973485089326, 5131676593756685549522564504727003861447389891839469018437277330988047271086971907217360711863971849879439418231726349935396008040776952541710218842744018, 8049060452950901277510497437779182190254362319091882684392717180429468875432078713802857488901441344429723298843967365750616860588029426099852763482179470, 2365060249260571713545479629411006471094806409182638354076861269679377537605360223984548798658469783472746989448405310909017645138161178501458084966625559, 7467521246204465304438401242342633361751371318557249418344587207503257890765643838557008735305668588521988487342275527781708126255070883848829062790678347, 5841608816993144092409175658260479687582056537041472535819914412630519543198558564258699185557903902095773598614097026740427138629173672250387442834578787, 3935779917509948624841228665498558015416911059417306651751360048412619176423173794541812556512582747588138532941031730797102738268660078594473168666677171, 1459083415233950534805962555425717865938763752937036513111696179351002303817986848490146888626704327653287774806488952733813718461674376764427084478395399, 6426876689549337938550615491086475536072547585103523407263007393570982327518298678278232288342601754164640081474537962710401178482959474762541185760732929, 5241364650650467046722868257809607948071188801137204831449976666385482519613365369974704486723941517654753205012497273820309153659423928739972270634209996, 6387483223002092292686097811446217867743566298067033295601210265979889577756648605354064672061975949925472022416479935990178719227937307079186916383092053, 170562164015232424518655058158727202269056868720093972639058422975773575660534168774299548952867348396798580779605954510297102765330549642318362861226163, 10004133230245713370426176448219282796530473722412487408402635996842671302539458739305597027107498342509248085998067976408732789438099488867425813748783724, 12325342879747412722323355648741345730921040452129462974449188258885453690169624888480720109964630270938743431623479816739889661554987977051169401841580388, 641543989928732942291347866597230552820621633110802944556141221591498546555080480758772801043509130524233886009444044150447511986129019395067102094826363]
# B = [108715652691370707411987210267535348806, 131676833696101475747102644851662113271, 122436706338521558335484593966234623745, 255864866572301552398412638474857375629, 81098761191414480003681301866161112100, 322322463176364397336266169283851913620, 198167679309202772183020662350938553923, 326360662842236388778385468938922853242, 241812832858991643670485138860832357660, 69768236619183466076110136290750715548, 32383134960394164339076842474280712870, 147747232748027508904245311745435517130, 25327826075608705748116808975774398964, 65295332681674581261444632606267440749, 236756211690281667988216748814564193312, 106435149910135092172124474857722935730, 270727089812520941022075406571244846193, 206881193220261276126028739930244917728, 131961838897694897398340205404861333362, 219211823942216355573832791993673934321, 150960424777134558142309786444952807101, 51112048255939343109218372373173385772, 182065623911902509203036774197184164110, 168420344895532090057957641972492853410, 301808673225362418769168353084541667053, 132272458662433671393247350648662880688, 495672626901999558635736361346563007, 182444159345379042372018248514964944782, 144584137563407779776361378564517880036, 338518705859818740467225748906995999694, 205885429741815676881969528495365151019, 233897982464483450790005953366237992668, 279307677123402840425362992920185630901, 133493426228159673166382443820069696429, 316624110847744871475435405969944304329, 187931604382397525131117897387179435812, 220019728924915067987393012581921164417]
# enc = b'cTmkMb\xfc\x05|\x1d\xc7\x13\xbaSe\xe0\xbd\xc0\xd9\xa3\x8cwo\x82yN[B&\x80\xd7KPwQ`\x9c\xbf<y\x8e\x8a\x97e\xa074\xb2'