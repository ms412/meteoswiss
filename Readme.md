https://www.meteoswiss.admin.ch/home.html?tab=overview


Some more information about the API:

It's the endpoint used by the iOS and Android app
Usually the plzDetail parameter is the postal code with 00 appended
example for 1950 Sion: https://app-prod-ws.meteoswiss-app.ch/v1/plzDetail?plz=195000
but for big cities like Lausanne it's 100101
You can find these codes using the following url by replacing la.json with the first two letters of the city: https://www.meteosuisse.admin.ch/etc/designs/meteoswiss/ajax/search/la.json
The API returns a number for the weather condition, you can find the corresponding icon by replacing the number at the end of this URL: https://www.meteosuisse.admin.ch/etc/designs/meteoswiss/assets/images/icons/meteo/weather-symbols/1.svg
And here are the descriptions of the weather conditions by ID:

<string name="wettersymboltexte_1">sunny</string>
<string name="wettersymboltexte_10">overcast, some sleet</string>
<string name="wettersymboltexte_101">clear</string>
<string name="wettersymboltexte_102">slightly overcast</string>
<string name="wettersymboltexte_103">heavy cloud formations</string>
<string name="wettersymboltexte_104">overcast</string>
<string name="wettersymboltexte_105">very cloudy</string>
<string name="wettersymboltexte_106">overcast, scattered showers</string>
<string name="wettersymboltexte_107">overcast, scattered rain and snow showers</string>
<string name="wettersymboltexte_108">overcast, snow showers</string>
<string name="wettersymboltexte_109">overcast, some showers</string>
<string name="wettersymboltexte_11">overcast, some snow showers</string>
<string name="wettersymboltexte_110">overcast, some rain and snow showers</string>
<string name="wettersymboltexte_111">overcast, some snow showers</string>
<string name="wettersymboltexte_112">slightly stormy</string>
<string name="wettersymboltexte_113">storms</string>
<string name="wettersymboltexte_114">very cloudy, light rain</string>
<string name="wettersymboltexte_115">very cloudy, light rain and snow  showers</string>
<string name="wettersymboltexte_116">very cloudy, light snowfall</string>
<string name="wettersymboltexte_117">very cloudy, intermittent rain</string>
<string name="wettersymboltexte_118">very cloudy, intermittant mixed rain and snowfall</string>
<string name="wettersymboltexte_119">very cloudy, intermittent snowfall</string>
<string name="wettersymboltexte_12">sunny intervals, chance of thunderstorms</string>
<string name="wettersymboltexte_120">very cloudy,  constant rain</string>
<string name="wettersymboltexte_121">very cloudy, frequent rain and snowfall</string>
<string name="wettersymboltexte_122">very cloudy, heavy snowfall</string>
<string name="wettersymboltexte_123">very cloudy, slightly stormy</string>
<string name="wettersymboltexte_124">very cloudy, stormy</string>
<string name="wettersymboltexte_125">very cloudy, storms</string>
<string name="wettersymboltexte_126">high cloud</string>
<string name="wettersymboltexte_127">stratus</string>
<string name="wettersymboltexte_128">fog</string>
<string name="wettersymboltexte_129">slightly overcast, scattered showers</string>
<string name="wettersymboltexte_13">sunny intervals, possible thunderstorms</string>
<string name="wettersymboltexte_130">slightly overcast, scattered snowfall</string>
<string name="wettersymboltexte_131">slightly overcast, rain and snow showers</string>
<string name="wettersymboltexte_132">slightly overcast, some showers</string>
<string name="wettersymboltexte_133">overcast, frequent snow showers</string>
<string name="wettersymboltexte_134">overcast, frequent snow showers</string>
<string name="wettersymboltexte_135">overcast with high cloud</string>
<string name="wettersymboltexte_14">very cloudy, light rain</string>
<string name="wettersymboltexte_15">very cloudy, light sleet</string>
<string name="wettersymboltexte_16">very cloudy, light snow showers</string>
<string name="wettersymboltexte_17">very cloudy, intermittent rain</string>
<string name="wettersymboltexte_18">very cloudy, intermittent sleet</string>
<string name="wettersymboltexte_19">very cloudy, intermittent snow</string>
<string name="wettersymboltexte_2">mostly sunny, some clouds</string>
<string name="wettersymboltexte_20">very overcast with rain</string>
<string name="wettersymboltexte_21">very overcast with frequent sleet</string>
<string name="wettersymboltexte_22">very overcast with heavy snow</string>
<string name="wettersymboltexte_23">very overcast, slight chance of storms</string>
<string name="wettersymboltexte_24">very overcast with storms</string>
<string name="wettersymboltexte_25">very cloudy, very stormy</string>
<string name="wettersymboltexte_26">high clouds</string>
<string name="wettersymboltexte_27">stratus</string>
<string name="wettersymboltexte_28">fog</string>
<string name="wettersymboltexte_29">Sunny intervals, scattered showers</string>
<string name="wettersymboltexte_3">partly sunny, thick passing clouds</string>
<string name="wettersymboltexte_30">Sunny intervals, scattered snow showers</string>
<string name="wettersymboltexte_31">Sunny intervals, scattered sleet</string>
<string name="wettersymboltexte_32">Sunny intervals, some showers</string>
<string name="wettersymboltexte_33">short sunny intervals, frequent rain</string>
<string name="wettersymboltexte_34">short sunny intervals, frequent snowfalls</string>
<string name="wettersymboltexte_35">overcast with high cloud</string>
<string name="wettersymboltexte_4">overcast</string>
<string name="wettersymboltexte_5">very cloudy</string>
<string name="wettersymboltexte_6">sunny intervals,  isolated showers</string>
<string name="wettersymboltexte_7">sunny intervals, isolated sleet</string>
<string name="wettersymboltexte_8">sunny intervals, snow showers</string>
<string name="wettersymboltexte_9">overcast, some rain showers</string>