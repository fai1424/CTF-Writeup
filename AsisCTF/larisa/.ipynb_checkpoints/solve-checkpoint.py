from Cryptodome.Util.number import *

print(1024 >> 1)
u = 1462429177173255359388007765931796537885368646963625242711326952977985471932962383861842635724040143033586225507124897993946275538644782337485276659791768803892242293535522679957964876776825548307042572518152706215000123872096447939862588392736653305289270336986724756913886373602016050815040147667630379593859685646307913471020561969933852495456652645591262189417744078633139731004839760821762709078987432999550663454348821414654652257866073987807333618308663409376712742627162896125313056171829232263020741802783450992451834392620606043876037571745527804406103083287186596413204262417693475997360716169601004
v = 3361480002432693752626969088049143371033687796839032797315025143270946165139685061767026950394284498430926616845318237749712235930625309923903553850166793512181385788796869552215035455995370731816925378753732950039662516557875218374075823193808692392905081204067496016151667029418998917540743277631790419809752354652686500452367372802836483170592925224959479584778030250914074383997961924181706306681930041686426001864642557173165132110893305941080323382987813126090590272821376238345672517574935462126595211630982601294558596563972548400634497302430346025087052735168147932593694561898028225523940866874133379
n = 4008883280270490147018156798752367239459738170301430156348460445088206527048348763760917689680659443318901951360516237262067529304338022837630483645196033621304254000080347982506422415455884933061116059048068199094286198189562171954474774550333796393036361152513608385296841124457358944339309759412021626022854509621495881349117414093445491445654319715891479654096144019797840785614103437600093538599616479514552612464205903106999476721076731416925688036797972413175747167321276835717505959961674004440955460813234396658192578904514644322909786797887720838286121169342271751904104529587650648676532260230880251
c = 3309629508959584128230612074347190739927545664904299989648238914737928604135368325911619522168319646327710121629807700297133099757696348608872841783442909500945895046635610910032194240479153787968351434814626345330003107353783812257020006242435243345046344898591276950746249307045935633972732008301954536072882886730280063790321460574169136949746594095419049316818205661247488681646844441794828909897999773387001878462330994053758731317170118624021445627807773860715311680550099039292463923535627372276120134300337541349809506039721311255832543793638212911911226396687521214715073293308087345418705502341630822

copy = u

while not isPrime(u+v):
    u += 1
print(copy-u)
print(isPrime(u+v))
e = u+v
print(n/e)

c = pow(m0, e, n)

c = m0**e mod n

c*xn