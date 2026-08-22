# -*- coding: utf-8 -*-
import json, math, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# ---------- 12 регионов ----------
REGIONS = [
 ("eu-north","Северная Европа","Европа"),
 ("eu-west","Западная Европа","Европа"),
 ("eu-central","Центральная Европа","Европа"),
 ("eu-south","Южная Европа","Европа"),
 ("eu-balkan","Юго-Восточная Европа (Балканы)","Европа"),
 ("eu-east","Восточная Европа","Европа"),
 ("as-north","Северная Азия (Сибирь)","Азия"),
 ("as-central","Центральная Азия","Азия"),
 ("as-west","Западная (Передняя) Азия","Азия"),
 ("as-south","Южная Азия","Азия"),
 ("as-southeast","Юго-Восточная Азия","Азия"),
 ("as-east","Восточная Азия","Азия"),
]

A3 = {
 # Северная Европа
 "NOR":"eu-north","SWE":"eu-north","FIN":"eu-north","DNK":"eu-north","ISL":"eu-north",
 "EST":"eu-north","LVA":"eu-north","LTU":"eu-north","FRO":"eu-north","ALD":"eu-north",
 # Западная Европа
 "GBR":"eu-west","IRL":"eu-west","FRA":"eu-west","BEL":"eu-west","NLD":"eu-west",
 "LUX":"eu-west","MCO":"eu-west","IMN":"eu-west","JEY":"eu-west","GGY":"eu-west",
 # Центральная Европа
 "DEU":"eu-central","POL":"eu-central","CZE":"eu-central","SVK":"eu-central","AUT":"eu-central",
 "CHE":"eu-central","HUN":"eu-central","SVN":"eu-central","LIE":"eu-central",
 # Южная Европа
 "ESP":"eu-south","PRT":"eu-south","ITA":"eu-south","MLT":"eu-south","AND":"eu-south",
 "SMR":"eu-south","VAT":"eu-south","GIB":"eu-south",
 # Балканы
 "GRC":"eu-balkan","HRV":"eu-balkan","BIH":"eu-balkan","SRB":"eu-balkan","MNE":"eu-balkan",
 "ALB":"eu-balkan","MKD":"eu-balkan","BGR":"eu-balkan","ROU":"eu-balkan","KOS":"eu-balkan",
 # Восточная Европа
 "UKR":"eu-east","BLR":"eu-east","MDA":"eu-east",
 # Центральная Азия
 "UZB":"as-central","TKM":"as-central","TJK":"as-central","KGZ":"as-central",
 # Западная Азия
 "GEO":"as-west","ARM":"as-west","AZE":"as-west","IRN":"as-west","IRQ":"as-west","SYR":"as-west",
 "LBN":"as-west","ISR":"as-west","PSX":"as-west","PSE":"as-west","JOR":"as-west","CYP":"as-west","CNM":"as-west","CYN":"as-west",
 "SAU":"as-west","YEM":"as-west","OMN":"as-west","ARE":"as-west","QAT":"as-west","BHR":"as-west","KWT":"as-west",
 # Южная Азия
 "IND":"as-south","PAK":"as-south","BGD":"as-south","NPL":"as-south","BTN":"as-south",
 "LKA":"as-south","MDV":"as-south","AFG":"as-south",
 # Юго-Восточная Азия
 "MMR":"as-southeast","THA":"as-southeast","LAO":"as-southeast","KHM":"as-southeast","VNM":"as-southeast",
 "MYS":"as-southeast","SGP":"as-southeast","IDN":"as-southeast","PHL":"as-southeast","BRN":"as-southeast","TLS":"as-southeast",
 # Восточная Азия
 "CHN":"as-east","MNG":"as-east","JPN":"as-east","PRK":"as-east","KOR":"as-east","TWN":"as-east","HKG":"as-east","MAC":"as-east",
}

RU_NAME = {
 "NOR":"Норвегия","SWE":"Швеция","FIN":"Финляндия","DNK":"Дания","ISL":"Исландия","EST":"Эстония",
 "LVA":"Латвия","LTU":"Литва","FRO":"Фарерские о-ва","ALD":"Аландские о-ва",
 "GBR":"Великобритания","IRL":"Ирландия","FRA":"Франция","BEL":"Бельгия","NLD":"Нидерланды",
 "LUX":"Люксембург","MCO":"Монако","IMN":"о. Мэн","JEY":"Джерси","GGY":"Гернси",
 "DEU":"Германия","POL":"Польша","CZE":"Чехия","SVK":"Словакия","AUT":"Австрия","CHE":"Швейцария",
 "HUN":"Венгрия","SVN":"Словения","LIE":"Лихтенштейн",
 "ESP":"Испания","PRT":"Португалия","ITA":"Италия","MLT":"Мальта","AND":"Андорра","SMR":"Сан-Марино",
 "VAT":"Ватикан","GIB":"Гибралтар",
 "GRC":"Греция","HRV":"Хорватия","BIH":"Босния и Герцеговина","SRB":"Сербия","MNE":"Черногория",
 "ALB":"Албания","MKD":"Северная Македония","BGR":"Болгария","ROU":"Румыния","KOS":"Косово",
 "UKR":"Украина","BLR":"Беларусь","MDA":"Молдова",
 "RUS":"Россия","TUR":"Турция","KAZ":"Казахстан",
 "UZB":"Узбекистан","TKM":"Туркменистан","TJK":"Таджикистан","KGZ":"Киргизия",
 "GEO":"Грузия","ARM":"Армения","AZE":"Азербайджан","IRN":"Иран","IRQ":"Ирак","SYR":"Сирия",
 "LBN":"Ливан","ISR":"Израиль","PSX":"Палестина","PSE":"Палестина","JOR":"Иордания","CYP":"Кипр","CNM":"Кипр","CYN":"Сев. Кипр",
 "SAU":"Саудовская Аравия","YEM":"Йемен","OMN":"Оман","ARE":"ОАЭ","QAT":"Катар","BHR":"Бахрейн","KWT":"Кувейт",
 "IND":"Индия","PAK":"Пакистан","BGD":"Бангладеш","NPL":"Непал","BTN":"Бутан","LKA":"Шри-Ланка",
 "MDV":"Мальдивы","AFG":"Афганистан",
 "MMR":"Мьянма","THA":"Таиланд","LAO":"Лаос","KHM":"Камбоджа","VNM":"Вьетнам","MYS":"Малайзия",
 "SGP":"Сингапур","IDN":"Индонезия","PHL":"Филиппины","BRN":"Бруней","TLS":"Восточный Тимор",
 "CHN":"Китай","MNG":"Монголия","JPN":"Япония","PRK":"КНДР","KOR":"Республика Корея","TWN":"Тайвань",
 "HKG":"Гонконг","MAC":"Макао",
}

# соседи вне Евразии — серый контекстный слой
CONTEXT = {"MAR","DZA","TUN","LBY","EGY","SDN","ERI","ETH","DJI","SOM","ESH","MRT","MLI","NER","TCD",
           "USA","CAN","GRL","AUS","PNG","NZL","PLW","KEN","UGA","SSD","CAF","NGA","BFA","SEN","GMB","GNB","GIN"}

# ---------- граница Европа/Азия: lon = f(lat) ----------
# Урал -> река Урал -> Каспий.  Ниже 47° с.ш. хвост задаётся отдельно для России и Казахстана.
DIVIDE = [(82,68.0),(70.5,67.0),(69.0,66.5),(66.0,63.5),(63.0,60.5),(60.0,59.5),
          (57.0,59.0),(55.0,59.2),(53.0,58.0),(51.2,58.5),(50.0,54.5),(48.5,52.6),(47.1,51.9)]
TUR_DIVIDE = [(43,29.2),(41.6,29.2),(41.25,29.15),(41.02,29.0),(40.75,28.0),
              (40.45,27.0),(40.30,26.7),(40.20,26.35),(40.05,26.15),(38,25.4)]

def divider(pts, tail_lat, tail_lon):
    pts = sorted(pts, key=lambda p:-p[0])
    def f(lat):
        if lat >= pts[0][0]: return pts[0][1]
        if lat <= tail_lat:  return tail_lon
        for i in range(len(pts)-1):
            a,b = pts[i], pts[i+1]
            if b[0] <= lat <= a[0]:
                t = (lat-b[0])/(a[0]-b[0]) if a[0]!=b[0] else 0
                return b[1] + t*(a[1]-b[1])
        return pts[-1][1]
    return f

F_RUS = divider(DIVIDE, 47.1, 52.0)   # Дагестан (48.5°в.д.) остаётся в Европе
F_KAZ = divider(DIVIDE, 47.1, 46.0)   # Мангышлак целиком в Азии
F_TUR = divider(TUR_DIVIDE, 38.0, 25.4)

def clip_ring(ring, f, keep_west):
    """Отсекает кольцо по линии lon=f(lat). Sutherland–Hodgman по монотонной границе."""
    def inside(p):
        lo = p[0] + 360.0 if p[0] < -100 else p[0]   # Чукотка: -170° -> 190°
        return (lo < f(p[1])) if keep_west else (lo >= f(p[1]))
    def cut(a, b):
        lo, hi = 0.0, 1.0
        for _ in range(24):
            m = (lo+hi)/2
            p = (a[0]+(b[0]-a[0])*m, a[1]+(b[1]-a[1])*m)
            if inside(p) == inside(a): lo = m
            else: hi = m
        t = (lo+hi)/2
        return (a[0]+(b[0]-a[0])*t, a[1]+(b[1]-a[1])*t)
    out = []
    n = len(ring)
    for i in range(n):
        cur, prv = ring[i], ring[i-1]
        ci, pi = inside(cur), inside(prv)
        if ci:
            if not pi: out.append(cut(prv, cur))
            out.append(cur)
        elif pi:
            out.append(cut(prv, cur))
    return out if len(out) >= 4 else None

# ---------- проекция Equal Earth ----------
LON0 = 80.0
A1,A2,A3c,A4 = 1.340264, -0.081106, 0.000893, 0.003796
S3 = math.sqrt(3)/2
def project(lon, lat):
    if lon < -100: lon += 360.0
    lam = math.radians(lon - LON0); phi = math.radians(lat)
    th = math.asin(max(-1,min(1,S3*math.sin(phi))))
    t2 = th*th; t3 = t2*th; t6 = t3*t3; t7 = t6*th; t8 = t6*t2; t9 = t8*th
    den = S3*(A1 + 3*A2*t2 + 7*A3c*t6 + 9*A4*t8)
    x = lam*math.cos(th)/den
    y = A1*th + A2*t3 + A3c*t7 + A4*t9
    return (x, y)

# кадр
X0,_ = project(-26, 40); X1,_ = project(192, 40)
_,Y1 = project(80, 82); _,Y0 = project(80, -12)
xs = [project(l, 40)[0] for l in (-26,192)]
XMIN = min(project(l, la)[0] for l in (-26,) for la in (0,20,40,60,80))
XMAX = max(project(l, la)[0] for l in (192,) for la in (0,20,40,60,80))
W = 2400.0
SC = W/(XMAX-XMIN)
H = (Y1-Y0)*SC
def pt(lon, lat):
    x,y = project(lon, lat)
    return ((x-XMIN)*SC, (Y1-y)*SC)

# ---------- упрощение ----------
def rdp(pts, eps):
    if len(pts) < 3: return pts
    stack=[(0,len(pts)-1)]; keep=[False]*len(pts); keep[0]=keep[-1]=True
    while stack:
        i,j = stack.pop()
        ax,ay = pts[i]; bx,by = pts[j]
        dx,dy = bx-ax, by-ay; d2 = dx*dx+dy*dy
        best,bi = -1,-1
        for k in range(i+1,j):
            px,py = pts[k]
            if d2 == 0: dist = (px-ax)**2+(py-ay)**2
            else:
                t = max(0,min(1,((px-ax)*dx+(py-ay)*dy)/d2))
                dist = (px-ax-t*dx)**2 + (py-ay-t*dy)**2
            if dist > best: best,bi = dist,k
        if best > eps*eps:
            keep[bi]=True; stack.append((i,bi)); stack.append((bi,j))
    return [p for p,k in zip(pts,keep) if k]

def path_of(rings, eps=1.1, close=True):
    out=[]
    for r in rings:
        p = [pt(x,y) for x,y in r]
        p = rdp(p, eps)
        if len(p) < (4 if close else 2): continue
        out.append("M"+" ".join(f"{a:.1f},{b:.1f}" for a,b in p)+("Z" if close else ""))
    return "".join(out)

def in_frame(ring):
    n=len(ring); 
    if n==0: return False
    la=sum(p[1] for p in ring)/n
    lo=sum((p[0]+360 if p[0]<-100 else p[0]) for p in ring)/n
    return -27 <= lo <= 193 and -12.5 <= la <= 83

def rings_of(geom):
    t,c = geom["type"], geom["coordinates"]
    if t == "Polygon": return [r for r in c]
    if t == "MultiPolygon": return [r for poly in c for r in poly]
    if t == "LineString": return [c]
    if t == "MultiLineString": return list(c)
    return []

_rings_of = rings_of
def rings_of(geom):
    return [r for r in _rings_of(geom) if in_frame(r)]

# ---------- страны ----------
data = json.load(open("countries.geojson"))
countries, context_paths = [], []
SPLIT = {"RUS":(F_RUS,"eu-east","as-north"), "TUR":(F_TUR,"eu-balkan","as-west"), "KAZ":(F_KAZ,"eu-east","as-central")}

for feat in data["features"]:
    p = feat["properties"]; a3 = p["ADM0_A3"]
    rings = rings_of(feat["geometry"])
    if a3 in SPLIT:
        f, reg_w, reg_e = SPLIT[a3]
        for keep_west, reg in ((True,reg_w),(False,reg_e)):
            cut = [c for c in (clip_ring(r, f, keep_west) for r in rings) if c]
            if not cut: continue
            d = path_of(cut)
            if d: countries.append({"id":a3+("_eu" if keep_west else "_as"),"n":RU_NAME[a3],
                                    "r":reg,"d":d,"split":True})
        continue
    reg = A3.get(a3)
    if reg:
        d = path_of(rings)
        if d: countries.append({"id":a3,"n":RU_NAME.get(a3,p.get("NAME_RU") or p["NAME"]),"r":reg,"d":d})
    elif a3 in CONTEXT:
        d = path_of(rings, eps=2.2)
        if d: context_paths.append(d)

# ---------- реки и озёра ----------
RU_RIV = {"Volga":"Волга","Danube":"Дунай","Rhein":"Рейн","Dnipro":"Днепр","Don":"Дон","Wisla":"Висла",
 "Loire":"Луара","Seine":"Сена","Elbe":"Эльба","Po":"По","Ob":"Обь","Ertis":"Иртыш","Yenisey":"Енисей",
 "Lena":"Лена","Amur":"Амур","Huang":"Хуанхэ","Yangtze":"Янцзы","Chang Jiang":"Янцзы","Mekong":"Меконг",
 "Ganges":"Ганг","Indus":"Инд","Brahmaputra":"Брахмапутра","Al Furat":"Евфрат","Firat":"Евфрат",
 "Tigris":"Тигр","Dijlah":"Тигр","Amu Darya":"Амударья","Syr Darya":"Сырдарья","Kolyma":"Колыма",
 "Ural":"Урал","Kama":"Кама","Angara":"Ангара","Vilyuy":"Вилюй","Aldan":"Алдан","Irtysh":"Иртыш",
 "Salween":"Салуин","Irrawaddy":"Иравади","Rhone":"Рона","Rhône":"Рона","Tagus":"Тахо","Ebro":"Эбро",
 "Oder":"Одра","Dniester":"Днестр","Neva":"Нева","Pechora":"Печора","Sev. Dvina":"Сев. Двина",
 "Selenge":"Селенга","Zeya":"Зея","Olenek":"Оленёк","Indigirka":"Индигирка","Yana":"Яна",
 "Narmada":"Нарма́да","Godavari":"Годавари","Krishna":"Кришна","Chao Phraya":"Менам","Xi":"Сицзян"}
riv = json.load(open("rivers.geojson"))
rivers=[]
for f in riv["features"]:
    pr = f["properties"]
    if (pr.get("scalerank") or 9) > 6: continue
    lines = rings_of(f["geometry"])
    ok=[l for l in lines if any(-30<=x<=192 or x<-140 for x,y in l) and any(-13<=y<=83 for x,y in l)]
    if not ok: continue
    d = path_of(ok, eps=1.4, close=False)
    if d: rivers.append({"d":d,"n":RU_RIV.get(pr.get("name") or "","")})

RU_LAKE = {"Lake Baikal":"оз. Байкал","Lake Ladoga":"Ладожское оз.","Lake Onega":"Онежское оз.",
 "Lake Balkhash":"оз. Балхаш","Issyk-Kul":"оз. Иссык-Куль","Lake Van":"оз. Ван","Lake Urmia":"оз. Урмия",
 "Aral Sea":"Аральское море","Caspian Sea":"","Lake Zaysan":"оз. Зайсан","Qinghai Hu":"оз. Кукунор",
 "Tonle Sap":"оз. Тонлесап","Lake Taymyr":"оз. Таймыр","Vänern":"оз. Венерн","Lake Khanka":"оз. Ханка",
 "Lake Peipus":"Чудское оз.","Rybinsk Reservoir":"Рыбинское вдхр.","Lake Tuz":"оз. Туз"}
lak = json.load(open("lakes.geojson"))
lakes=[]
for f in lak["features"]:
    pr = f["properties"]; nm = pr.get("name") or ""
    if (pr.get("scalerank") or 9) > 3 and nm not in RU_LAKE: continue
    rr = rings_of(f["geometry"])
    ok=[r for r in rr if any(-30<=x<=192 for x,y in r) and any(-13<=y<=83 for x,y in r)]
    if not ok: continue
    d = path_of(ok, eps=0.9)
    if d: lakes.append({"d":d,"n":RU_LAKE.get(nm,"")})

# ---------- подписи ----------
import labels as L
def mk(items, kind):
    r=[]
    for it in items:
        lat, lon, txt = it[0], it[1], it[2]
        if not txt: continue
        sz = it[3] if len(it)>3 else 2
        x,y = pt(lon, lat)
        r.append({"x":round(x,1),"y":round(y,1),"t":txt,"s":sz,"k":kind})
    return r
lbl = (mk(L.OCEANS,"ocean")+mk(L.SEAS,"sea")+mk(L.GULFS,"gulf")+
       mk([(a,b,c,2) for a,b,c in L.STRAITS],"strait")+
       mk(L.MOUNTAINS,"mtn")+mk(L.PLAINS,"plain")+mk(L.DESERTS,"desert")+
       mk(L.PENINSULAS,"pen")+mk(L.ISLANDS,"isl")+
       mk([(a,b,c,2) for a,b,c in L.CAPES],"cape"))

# точки подписей стран: LABEL_X/LABEL_Y из Natural Earth
anchors = {}
for feat in data["features"]:
    pr = feat["properties"]; a3 = pr["ADM0_A3"]
    lx, ly = pr.get("LABEL_X"), pr.get("LABEL_Y")
    if a3 in A3 and lx is not None and ly is not None:
        x,y = pt(lx, ly); anchors[a3] = [round(x,1), round(y,1)]
for cid, lat, lon, nm in L.SPLIT_LABELS:
    x,y = pt(lon, lat); anchors[cid] = [round(x,1), round(y,1)]
for c in countries:
    a = anchors.get(c["id"])
    if a: c["a"] = a

# метки рек / озёр — середина самой длинной линии
def mid_of(d):
    best=None
    for seg in d.split("M")[1:]:
        pts=[tuple(map(float,q.split(","))) for q in seg.rstrip("Z").split()]
        if best is None or len(pts)>len(best): best=pts
    if not best: return None
    return [round(best[len(best)//2][0],1), round(best[len(best)//2][1],1)]
for r in rivers:
    if r["n"]:
        m = mid_of(r["d"])
        if m: r["a"]=m
for k in lakes:
    if k["n"]:
        m = mid_of(k["d"])
        if m: k["a"]=m

# ---------- линия Европа/Азия ----------
DIVIDE_LINE = [(70.5,67.5),(69.0,66.5),(66.0,63.5),(63.0,60.5),(60.0,59.5),(57.0,59.0),
 (55.0,59.2),(53.0,58.0),(51.2,58.5),(50.0,54.5),(48.5,52.6),(47.1,51.9),
 (45.5,49.5),(44.6,47.6),(44.3,47.0),(45.0,44.8),(45.6,42.2),(46.2,39.3),
 (45.4,36.6),(44.5,34.0),(43.0,32.0),(41.8,30.0),(41.25,29.15),(41.02,29.0),(40.75,28.0),
 (40.45,27.0),(40.30,26.7),(40.20,26.35),(40.05,26.15),(39.0,25.5),(36.2,25.0)]
divide_d = "M"+" ".join("%.1f,%.1f" % pt(lo,la) for la,lo in DIVIDE_LINE)

# ---------- кегль подписи страны ----------
import re as _re
for c in countries:
    # кегль — по самому крупному куску, иначе Канары раздувают Испанию
    w_ = h_ = 0.0
    for seg in c["d"].split("M")[1:]:
        nums = _re.findall(r"(-?[\d.]+),(-?[\d.]+)", seg)
        if not nums: continue
        xs=[float(a) for a,b in nums]; ys=[float(b) for a,b in nums]
        sw, sh = max(xs)-min(xs), max(ys)-min(ys)
        if sw*sh > w_*h_: w_, h_ = sw, sh
    fs = max(10.5, min(31.0, (w_*h_)**0.5*0.147))
    c["fs"] = round(fs,1)
    c["mz"] = 1 if fs > 16.0 else (2.0 if fs > 12.4 else 3.2)

out = {"w":round(W),"h":round(H),"regions":REGIONS,"countries":countries,
       "context":context_paths,"rivers":rivers,"lakes":lakes,"labels":lbl,"divide":divide_d}
json.dump(out, open("map.json","w"), ensure_ascii=False, separators=(",",":"))
print("size", os.path.getsize("map.json")//1024, "KB")
print("W,H", round(W), round(H))
print("countries", len(countries), "rivers", len(rivers), "lakes", len(lakes), "context", len(context_paths))
missing = sorted(set(A3)-set(c["id"] for c in countries))
print("не найдены:", missing)


# ---------- самопроверка ----------
def _check():
    def side(f, lon, lat):
        lo = lon + 360.0 if lon < -100 else lon
        return "EU" if lo < f(lat) else "AS"
    cases = [
        (F_RUS,  37.6, 55.8, "EU", "Москва"),
        (F_RUS,  60.6, 56.8, "AS", "Екатеринбург (за Уралом)"),
        (F_RUS,  56.2, 58.0, "EU", "Пермь (перед Уралом)"),
        (F_RUS,-173.3, 64.7, "AS", "Анадырь / Чукотка"),
        (F_RUS,  47.5, 42.9, "EU", "Махачкала, Дагестан"),
        (F_RUS,  39.7, 47.2, "EU", "Ростов-на-Дону"),
        (F_KAZ,  51.9, 47.1, "AS", "Атырау, правый берег"),
        (F_KAZ,  50.3, 51.2, "EU", "Уральск"),
        (F_KAZ,  71.4, 51.1, "AS", "Астана"),
        (F_TUR,  28.98, 41.04, "EU", "Стамбул, Бейоглу — европейский берег"),
        (F_TUR,  29.02, 41.02, "AS", "Стамбул, Ускюдар — азиатский берег"),
        (F_TUR,  32.9, 39.9, "AS", "Анкара"),
    ]
    for f, lon, lat, want, who in cases:
        got = side(f, lon, lat)
        assert got == want, "%s: получилось %s, ожидалось %s" % (who, got, want)
    assert set(c["id"] for c in countries) >= set(["RUS_eu","RUS_as","TUR_eu","TUR_as","KAZ_eu","KAZ_as"])
    import re as _r
    xs = [float(a) for a,_ in _r.findall(r"(-?[\d.]+),(-?[\d.]+)",
          next(c for c in countries if c["id"]=="RUS_eu")["d"])]
    assert max(xs) - min(xs) < 700, "в RUS_eu попала азиатская часть"
    print("самопроверка: разрез Европа/Азия — %d контрольных точек, все верны" % len(cases))

if __name__ == "__main__":
    _check()
