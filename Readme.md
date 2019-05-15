https://www.meteoswiss.admin.ch/home.html?tab=overview

https://github.com/okaufmann/swiss-weather-api/blob/master/API.md

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

Hardcoded URL's
http://app-prod-static.meteoswiss.ch/	Not a known malware domain (scanned using Google Safe Browsing API)
http://app-prod-static.meteoswiss.ch/altitudeForecast.json	Not a known malware domain (scanned using Google Safe Browsing API)
http://app-prod-static.meteoswiss.ch/currentWeather.json	Not a known malware domain (scanned using Google Safe Browsing API)
http://app-prod-static.meteoswiss.ch/forecast_	Not a known malware domain (scanned using Google Safe Browsing API)
http://app-prod-static.meteoswiss.ch/forecast.json	Not a known malware domain (scanned using Google Safe Browsing API)
http://app-prod-static.meteoswiss.ch/generalForecast_	Not a known malware domain (scanned using Google Safe Browsing API)
http://app-prod-static.meteoswiss.ch/isobaren.jpg	Not a known malware domain (scanned using Google Safe Browsing API)
http://app-prod-static.meteoswiss.ch/meteo.cosmo.cloud.current.zip	Not a known malware domain (scanned using Google Safe Browsing API)
http://app-prod-static.meteoswiss.ch/meteo.cosmo.temp.current.zip	Not a known malware domain (scanned using Google Safe Browsing API)
http://app-prod-static.meteoswiss.ch/meteo.ir.alpen.current.zip	Not a known malware domain (scanned using Google Safe Browsing API)
http://app-prod-static.meteoswiss.ch/meteo.ir.europe.current.zip	Not a known malware domain (scanned using Google Safe Browsing API)
http://app-prod-static.meteoswiss.ch/meteo.radar.precip.current.zip	Not a known malware domain (scanned using Google Safe Browsing API)
http://app-prod-static.meteoswiss.ch/meteo.vis.schweiz.current.zip	Not a known malware domain (scanned using Google Safe Browsing API)
http://app-prod-static.meteoswiss.ch/other_warnings_	Not a known malware domain (scanned using Google Safe Browsing API)
http://app-prod-static.meteoswiss.ch/radarOverview.png	Not a known malware domain (scanned using Google Safe Browsing API)
http://app-prod-static.meteoswiss.ch/regionForecast.json	Not a known malware domain (scanned using Google Safe Browsing API)
http://app-prod-static.meteoswiss.ch/storm_bulletin_	Not a known malware domain (scanned using Google Safe Browsing API)
http://app-prod-static.meteoswiss.ch/warning_forecast_	Not a known malware domain (scanned using Google Safe Browsing API)
http://app-prod-static.meteoswiss.ch/warningOverview.jpg	Not a known malware domain (scanned using Google Safe Browsing API)
http://app-prod-static.meteoswiss.ch/warnings_	Not a known malware domain (scanned using Google Safe Browsing API)
http://app-prod-ws.meteoswiss.ch/	Not a known malware domain (scanned using Google Safe Browsing API)
http://app-prod-ws.meteoswiss.ch/cloudFileList	Not a known malware domain (scanned using Google Safe Browsing API)
http://app-prod-ws.meteoswiss.ch/forecast	Not a known malware domain (scanned using Google Safe Browsing API)
http://app-prod-ws.meteoswiss.ch/forecast?lat	Not a known malware domain (scanned using Google Safe Browsing API)
http://app-prod-ws.meteoswiss.ch/forecast?plz	Not a known malware domain (scanned using Google Safe Browsing API)
http://app-prod-ws.meteoswiss.ch/irAlpenFileList	Not a known malware domain (scanned using Google Safe Browsing API)
http://app-prod-ws.meteoswiss.ch/irEuropeFileList	Not a known malware domain (scanned using Google Safe Browsing API)
http://app-prod-ws.meteoswiss.ch/overview	Not a known malware domain (scanned using Google Safe Browsing API)
http://app-prod-ws.meteoswiss.ch/overview?lat	Not a known malware domain (scanned using Google Safe Browsing API)
http://app-prod-ws.meteoswiss.ch/overview?plz	Not a known malware domain (scanned using Google Safe Browsing API)
http://app-prod-ws.meteoswiss.ch/overview?wpplz=327000&ws;	Not a known malware domain (scanned using Google Safe Browsing API)
http://app-prod-ws.meteoswiss.ch/plzDetail?plz	Not a known malware domain (scanned using Google Safe Browsing API)
http://app-prod-ws.meteoswiss.ch/plzOverview?plz	Not a known malware domain (scanned using Google Safe Browsing API)
http://app-prod-ws.meteoswiss.ch/precipitationFileList	Not a known malware domain (scanned using Google Safe Browsing API)
http://app-prod-ws.meteoswiss.ch/register	Not a known malware domain (scanned using Google Safe Browsing API)
http://app-prod-ws.meteoswiss.ch/temperatureFileList	Not a known malware domain (scanned using Google Safe Browsing API)
http://app-prod-ws.meteoswiss.ch/verlaufPrognose?plz	Not a known malware domain (scanned using Google Safe Browsing API)
http://app-prod-ws.meteoswiss.ch/verlauf?station	Not a known malware domain (scanned using Google Safe Browsing API)
http://app-prod-ws.meteoswiss.ch/visSchweizFileList	Not a known malware domain (scanned using Google Safe Browsing API)
http://checkip.dyndns.org	Not a known malware domain (scanned using Google Safe Browsing API)
http://meteoswiss.ch/app	Not a known malware domain (scanned using Google Safe Browsing API)
http://schemas.android.com/apk/res/android	Not a known malware domain (scanned using Google Safe Browsing API)
http://schemas.android.com/apk/res/ch.admin.meteoswiss	Not a known malware domain (scanned using Google Safe Browsing API)
http://smaapp-dev.ubique.ch:8080/meteoschweiz-ws/	Not a known malware domain (scanned using Google Safe Browsing API)
http://smaapp.s3.amazonaws.com/	Not a known malware domain (scanned using Google Safe Browsing API)
https://ssl.google-analytics.com/collect	Not a known malware domain (scanned using Google Safe Browsing API)
http://www.google-analytics.com/collect	Not a known malware domain (scanned using Google Safe Browsing API)
http://www.meteoschweiz.admin.ch/web/de/contact.html?referer	Not a known malware domain (scanned using Google Safe Browsing API)
http://www.meteoschweiz.admin.ch/web/de/gefahren/details.html	Not a known malware domain (scanned using Google Safe Browsing API)
http://www.meteoschweiz.admin.ch/web/de/legal.html	Not a known malware domain (scanned using Google Safe Browsing API)
http://www.meteoschweiz.admin.ch/web/de/meteoschweiz/portrait.html	Not a known malware domain (scanned using Google Safe Browsing API)
http://www.meteoschweiz.admin.ch/web/en/contact.html?referer	Not a known malware domain (scanned using Google Safe Browsing API)
http://www.meteoschweiz.admin.ch/web/en/danger/details.html	Not a known malware domain (scanned using Google Safe Browsing API)
http://www.meteoschweiz.admin.ch/web/en/legal.html	Not a known malware domain (scanned using Google Safe Browsing API)
http://www.meteoschweiz.admin.ch/web/en/meteoswiss/portrait.html	Not a known malware domain (scanned using Google Safe Browsing API)
http://www.meteoschweiz.admin.ch/web/fr/contact.html?referer	Not a known malware domain (scanned using Google Safe Browsing API)
http://www.meteoschweiz.admin.ch/web/fr/dangers/details.html	Not a known malware domain (scanned using Google Safe Browsing API)
http://www.meteoschweiz.admin.ch/web/fr/legal.html	Not a known malware domain (scanned using Google Safe Browsing API)
http://www.meteoschweiz.admin.ch/web/fr/meteosuisse/portrait.html	Not a known malware domain (scanned using Google Safe Browsing API)
http://www.meteoschweiz.admin.ch/web/it/contact.html?referer	Not a known malware domain (scanned using Google Safe Browsing API)
http://www.meteoschweiz.admin.ch/web/it/legal.html	Not a known malware domain (scanned using Google Safe Browsing API)
http://www.meteoschweiz.admin.ch/web/it/meteosvizzera/ritratto.html	Not a known malware domain (scanned using Google Safe Browsing API)
http://www.meteoschweiz.admin.ch/web/it/pericoli/details.html	Not a known malware domain (scanned using Google Safe Browsing API)
http://www.ubique.ch/	Not a known malware domain (scanned using Google Safe Browsing API)
http://www.w3.org/1999/xlink	Not a known malware domain (scanned using Google Safe Browsing API)
http://www.w3.org/2000/svg	Not a known malware domain (scanned using Google Safe Browsing API)
http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd	Not a known malware domain (scanned using Google Safe Browsing API)


http://
http://%s
http://hostname/?
http://schemas.android.com/apk/res/android
http://www.google-analytics.com
http://www.meteoschweiz.admin.ch
http://www.meteoschweiz.admin.ch/
https://
https://app-measurement.com/a
https://app-prod-ws.meteoswiss-app.ch/v1/blog/comment
https://app-prod-ws.meteoswiss-app.ch/v1/currentweather?ws=
https://app-prod-ws.meteoswiss-app.ch/v1/forecast?plz=
https://app-prod-ws.meteoswiss-app.ch/v1/hagel
https://app-prod-ws.meteoswiss-app.ch/v1/plzDetail?plz=
https://app-prod-ws.meteoswiss-app.ch/v1/plzOverview?plz=
https://app-prod-ws.meteoswiss-app.ch/v1/register
https://app-prod-ws.meteoswiss-app.ch/v1/registerq
https://app-prod-ws.meteoswiss-app.ch/v1/stationOverview?station=
https://app-prod-ws.meteoswiss-app.ch/v1/vorortdetail?plz=
https://e.crashlytics.com/spi/v2/events
https://logs.meteoswiss-app.ch/piwik.php
https://pagead2.googlesyndication.com/pagead/gen_204?id=gmob-apps
https://play.google.com/store/apps/details?id=ch.ti.oasi.android.airquality
https://plus.google.com/
https://s3-eu-central-1.amazonaws.com/app-prod-static-fra.meteoswiss-app.ch/v1/
https://s3-eu-central-1.amazonaws.com/app-prod-static-fra.meteoswiss-app.ch/v1/aha_
https://s3-eu-central-1.amazonaws.com/app-prod-static-fra.meteoswiss-app.ch/v1/altitudeForecast.json
https://s3-eu-central-1.amazonaws.com/app-prod-static-fra.meteoswiss-app.ch/v1/animation_overview.json
https://s3-eu-central-1.amazonaws.com/app-prod-static-fra.meteoswiss-app.ch/v1/blog/
https://s3-eu-central-1.amazonaws.com/app-prod-static-fra.meteoswiss-app.ch/v1/blog/blog_homescreen_
https://s3-eu-central-1.amazonaws.com/app-prod-static-fra.meteoswiss-app.ch/v1/blog/blog_other_categories_
https://s3-eu-central-1.amazonaws.com/app-prod-static-fra.meteoswiss-app.ch/v1/blog/blog_overview_
https://s3-eu-central-1.amazonaws.com/app-prod-static-fra.meteoswiss-app.ch/v1/blog/blog_weather_today_
https://s3-eu-central-1.amazonaws.com/app-prod-static-fra.meteoswiss-app.ch/v1/currentPrecipitationHomescreen.png
https://s3-eu-central-1.amazonaws.com/app-prod-static-fra.meteoswiss-app.ch/v1/currentWeather.json
https://s3-eu-central-1.amazonaws.com/app-prod-static-fra.meteoswiss-app.ch/v1/currentWeatherHomescreen_
https://s3-eu-central-1.amazonaws.com/app-prod-static-fra.meteoswiss-app.ch/v1/current_ir_alpen_2_fileList.json
https://s3-eu-central-1.amazonaws.com/app-prod-static-fra.meteoswiss-app.ch/v1/current_ir_europe_2_fileList.json
https://s3-eu-central-1.amazonaws.com/app-prod-static-fra.meteoswiss-app.ch/v1/current_vis_schweiz_2_fileList.json
https://s3-eu-central-1.amazonaws.com/app-prod-static-fra.meteoswiss-app.ch/v1/db.sqlite
https://s3-eu-central-1.amazonaws.com/app-prod-static-fra.meteoswiss-app.ch/v1/dbinfo.json
https://s3-eu-central-1.amazonaws.com/app-prod-static-fra.meteoswiss-app.ch/v1/forecast_
https://s3-eu-central-1.amazonaws.com/app-prod-static-fra.meteoswiss-app.ch/v1/forecast_homescreen.json
https://s3-eu-central-1.amazonaws.com/app-prod-static-fra.meteoswiss-app.ch/v1/forecast_v4.json
https://s3-eu-central-1.amazonaws.com/app-prod-static-fra.meteoswiss-app.ch/v1/generalForecast_
https://s3-eu-central-1.amazonaws.com/app-prod-static-fra.meteoswiss-app.ch/v1/healthHomescreenV2_
https://s3-eu-central-1.amazonaws.com/app-prod-static-fra.meteoswiss-app.ch/v1/isobaren_
https://s3-eu-central-1.amazonaws.com/app-prod-static-fra.meteoswiss-app.ch/v1/other_warnings_
https://s3-eu-central-1.amazonaws.com/app-prod-static-fra.meteoswiss-app.ch/v1/pollen_animation_overview.json
https://s3-eu-central-1.amazonaws.com/app-prod-static-fra.meteoswiss-app.ch/v1/pollen_text_forecast_
https://s3-eu-central-1.amazonaws.com/app-prod-static-fra.meteoswiss-app.ch/v1/regionForecast_v3.json
https://s3-eu-central-1.amazonaws.com/app-prod-static-fra.meteoswiss-app.ch/v1/sov_bcm_
https://s3-eu-central-1.amazonaws.com/app-prod-static-fra.meteoswiss-app.ch/v1/stationimages/
https://s3-eu-central-1.amazonaws.com/app-prod-static-fra.meteoswiss-app.ch/v1/storm_bulletin2_
https://s3-eu-central-1.amazonaws.com/app-prod-static-fra.meteoswiss-app.ch/v1/street_
https://s3-eu-central-1.amazonaws.com/app-prod-static-fra.meteoswiss-app.ch/v1/warningOverviewHomescreen.json
https://s3-eu-central-1.amazonaws.com/app-prod-static-fra.meteoswiss-app.ch/v1/warnings_with_outlook_with_naturalhazards_
https://s3-eu-central-1.amazonaws.com/app-prod-static-fra.meteoswiss-app.ch/v1/webcam_
https://s3-eu-central-1.amazonaws.com/app-prod-static-fra.meteoswiss-app.ch/v1/webcam_latest_
https://s3-eu-central-1.amazonaws.com/app-prod-static-fra.meteoswiss-app.ch/v1/webcam_overview.json
https://settings.crashlytics.com/spi/v2/platforms/android/apps/%s/settings
https://ssl.google-analytics.com
https://www.google.com
https://www.googleapis.com/auth/games
https://www.googleapis.com/auth/games_lite


ttps://www.meteoschweiz.admin.ch/product/output/measured-values-v3/map/version__20190513_1626/de/chartPaths.json