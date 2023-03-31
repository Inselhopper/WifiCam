
#include "WifiCam.hpp"
#include <WiFi.h>

//static const char* WIFI_SSID = "FRITZ!Box 7490";
//static const char* WIFI_PASS = "32579960905241362629";

static const char* WIFI_SSID = "WLAN-366385";
static const char* WIFI_PASS = "8382203915071243";

esp32cam::Resolution initialResolution;

WebServer server(80);

void
setup()
{
  Serial.begin(115200);
  Serial.println();
  delay(2000);

  WiFi.persistent(false);
  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_SSID, WIFI_PASS);
  if (WiFi.waitForConnectResult() != WL_CONNECTED) {
    Serial.println("WiFi failure");
    delay(5000);
    ESP.restart();
  }
  Serial.println("WiFi connected");

  {
    using namespace esp32cam;

    initialResolution = Resolution::find(1024, 768);

    Config cfg;
    cfg.setPins(pins::AiThinker);
    cfg.setResolution(initialResolution);
    cfg.setJpeg(80);

    bool ok = Camera.begin(cfg);
    if (!ok) {
      Serial.println("camera initialize failure");
      delay(5000);
      ESP.restart();
    }
    Serial.println("camera initialize success");
  }

  Serial.println("camera starting");
  Serial.print("http://");
  Serial.println(WiFi.localIP());

  addRequestHandlers();
  server.begin();
}

void
loop()
{
  server.handleClient();
}
