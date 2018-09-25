# Congressional Record Data
Extract data from https://data.stanford.edu/congress_text here.

TODO: give proper file structure
.
├── audit
│   ├── audit
│   │   └── audit
│   │       ├── parsing
│   │       │   ├── auto
│   │       │   │   ├── hein-bound
│   │       │   │   │   ├── descr_01101920.txt
│   │       │   │   │   ├── descr_01111900.txt
│   │       │   │   │   ├── descr_01111910.txt
│   │       │   │   │   ├── descr_01121950.txt
│   │       │   │   │   ├── descr_01131880.txt
│   │       │   │   │   ├── descr_01131930.txt
│   │       │   │   │   ├── descr_01161890.txt
│   │       │   │   │   ├── descr_01161940.txt
│   │       │   │   │   ├── descr_01181960.txt
│   │       │   │   │   ├── descr_01202010.txt
│   │       │   │   │   ├── descr_01231980.txt
│   │       │   │   │   ├── descr_01271970.txt
│   │       │   │   │   ├── descr_01311990.txt
│   │       │   │   │   ├── descr_02022000.txt
│   │       │   │   │   ├── descr_03301920.txt
│   │       │   │   │   ├── descr_03311900.txt
│   │       │   │   │   ├── descr_04051880.txt
│   │       │   │   │   ├── descr_04091910.txt
│   │       │   │   │   ├── descr_04171930.txt
│   │       │   │   │   ├── descr_05091900.txt
│   │       │   │   │   ├── descr_05101960.txt
│   │       │   │   │   ├── descr_05111920.txt
│   │       │   │   │   ├── descr_05131880.txt
│   │       │   │   │   ├── descr_05141900.txt
│   │       │   │   │   ├── descr_05151920.txt
│   │       │   │   │   ├── descr_05191880.txt
│   │       │   │   │   ├── descr_05191910.txt
│   │       │   │   │   ├── descr_05241910.txt
│   │       │   │   │   ├── descr_05261950.txt
│   │       │   │   │   ├── descr_05291890.txt
│   │       │   │   │   ├── descr_06021980.txt
│   │       │   │   │   ├── descr_06031940.txt
│   │       │   │   │   ├── descr_06101930.txt
│   │       │   │   │   ├── descr_06111990.txt
│   │       │   │   │   ├── descr_06141930.txt
│   │       │   │   │   ├── descr_06192000.txt
│   │       │   │   │   ├── descr_06221970.txt
│   │       │   │   │   ├── descr_06252010.txt
│   │       │   │   │   ├── descr_07051960.txt
│   │       │   │   │   ├── descr_07111960.txt
│   │       │   │   │   ├── descr_08031950.txt
│   │       │   │   │   ├── descr_08091890.txt
│   │       │   │   │   ├── descr_08101950.txt
│   │       │   │   │   ├── descr_08161890.txt
│   │       │   │   │   ├── descr_08221980.txt
│   │       │   │   │   ├── descr_08281980.txt
│   │       │   │   │   ├── descr_08301940.txt
│   │       │   │   │   ├── descr_08311970.txt
│   │       │   │   │   ├── descr_09061990.txt
│   │       │   │   │   ├── descr_09071940.txt
│   │       │   │   │   ├── descr_09101970.txt
│   │       │   │   │   ├── descr_09131990.txt
│   │       │   │   │   ├── descr_09212000.txt
│   │       │   │   │   ├── descr_09272000.txt
│   │       │   │   │   ├── descr_09272010.txt
│   │       │   │   │   ├── descr_10012010.txt
│   │       │   │   │   ├── speeches_01101920.txt
│   │       │   │   │   ├── speeches_01111900.txt
│   │       │   │   │   ├── speeches_01111910.txt
│   │       │   │   │   ├── speeches_01121950.txt
│   │       │   │   │   ├── speeches_01131880.txt
│   │       │   │   │   ├── speeches_01131930.txt
│   │       │   │   │   ├── speeches_01161890.txt
│   │       │   │   │   ├── speeches_01161940.txt
│   │       │   │   │   ├── speeches_01181960.txt
│   │       │   │   │   ├── speeches_01202010.txt
│   │       │   │   │   ├── speeches_01231980.txt
│   │       │   │   │   ├── speeches_01271970.txt
│   │       │   │   │   ├── speeches_01311990.txt
│   │       │   │   │   ├── speeches_02022000.txt
│   │       │   │   │   ├── speeches_03301920.txt
│   │       │   │   │   ├── speeches_03311900.txt
│   │       │   │   │   ├── speeches_04051880.txt
│   │       │   │   │   ├── speeches_04091910.txt
│   │       │   │   │   ├── speeches_04171930.txt
│   │       │   │   │   ├── speeches_05091900.txt
│   │       │   │   │   ├── speeches_05101960.txt
│   │       │   │   │   ├── speeches_05111920.txt
│   │       │   │   │   ├── speeches_05131880.txt
│   │       │   │   │   ├── speeches_05141900.txt
│   │       │   │   │   ├── speeches_05151920.txt
│   │       │   │   │   ├── speeches_05191880.txt
│   │       │   │   │   ├── speeches_05191910.txt
│   │       │   │   │   ├── speeches_05241910.txt
│   │       │   │   │   ├── speeches_05261950.txt
│   │       │   │   │   ├── speeches_05291890.txt
│   │       │   │   │   ├── speeches_06021980.txt
│   │       │   │   │   ├── speeches_06031940.txt
│   │       │   │   │   ├── speeches_06101930.txt
│   │       │   │   │   ├── speeches_06111990.txt
│   │       │   │   │   ├── speeches_06141930.txt
│   │       │   │   │   ├── speeches_06192000.txt
│   │       │   │   │   ├── speeches_06221970.txt
│   │       │   │   │   ├── speeches_06252010.txt
│   │       │   │   │   ├── speeches_07051960.txt
│   │       │   │   │   ├── speeches_07111960.txt
│   │       │   │   │   ├── speeches_08031950.txt
│   │       │   │   │   ├── speeches_08091890.txt
│   │       │   │   │   ├── speeches_08101950.txt
│   │       │   │   │   ├── speeches_08161890.txt
│   │       │   │   │   ├── speeches_08221980.txt
│   │       │   │   │   ├── speeches_08281980.txt
│   │       │   │   │   ├── speeches_08301940.txt
│   │       │   │   │   ├── speeches_08311970.txt
│   │       │   │   │   ├── speeches_09061990.txt
│   │       │   │   │   ├── speeches_09071940.txt
│   │       │   │   │   ├── speeches_09101970.txt
│   │       │   │   │   ├── speeches_09131990.txt
│   │       │   │   │   ├── speeches_09212000.txt
│   │       │   │   │   ├── speeches_09272000.txt
│   │       │   │   │   ├── speeches_09272010.txt
│   │       │   │   │   └── speeches_10012010.txt
│   │       │   │   └── hein-daily
│   │       │   │       ├── descr_01111995.txt
│   │       │   │       ├── descr_01132015.txt
│   │       │   │       ├── descr_01212010.txt
│   │       │   │       ├── descr_01291985.txt
│   │       │   │       ├── descr_01311990.txt
│   │       │   │       ├── descr_01312005.txt
│   │       │   │       ├── descr_02012000.txt
│   │       │   │       ├── descr_06092010.txt
│   │       │   │       ├── descr_06102015.txt
│   │       │   │       ├── descr_06121990.txt
│   │       │   │       ├── descr_06162000.txt
│   │       │   │       ├── descr_06212005.txt
│   │       │   │       ├── descr_06221995.txt
│   │       │   │       ├── descr_06271985.txt
│   │       │   │       ├── descr_09101990.txt
│   │       │   │       ├── descr_09141990.txt
│   │       │   │       ├── descr_09172015.txt
│   │       │   │       ├── descr_09202000.txt
│   │       │   │       ├── descr_09202010.txt
│   │       │   │       ├── descr_09242010.txt
│   │       │   │       ├── descr_09252015.txt
│   │       │   │       ├── descr_09262000.txt
│   │       │   │       ├── descr_09272005.txt
│   │       │   │       ├── descr_09281995.txt
│   │       │   │       ├── descr_10032005.txt
│   │       │   │       ├── descr_10051985.txt
│   │       │   │       ├── descr_10091985.txt
│   │       │   │       ├── descr_10121995.txt
│   │       │   │       ├── speeches_01111995.txt
│   │       │   │       ├── speeches_01132015.txt
│   │       │   │       ├── speeches_01212010.txt
│   │       │   │       ├── speeches_01291985.txt
│   │       │   │       ├── speeches_01311990.txt
│   │       │   │       ├── speeches_01312005.txt
│   │       │   │       ├── speeches_02012000.txt
│   │       │   │       ├── speeches_06092010.txt
│   │       │   │       ├── speeches_06102015.txt
│   │       │   │       ├── speeches_06121990.txt
│   │       │   │       ├── speeches_06162000.txt
│   │       │   │       ├── speeches_06212005.txt
│   │       │   │       ├── speeches_06221995.txt
│   │       │   │       ├── speeches_06271985.txt
│   │       │   │       ├── speeches_09101990.txt
│   │       │   │       ├── speeches_09141990.txt
│   │       │   │       ├── speeches_09172015.txt
│   │       │   │       ├── speeches_09202000.txt
│   │       │   │       ├── speeches_09202010.txt
│   │       │   │       ├── speeches_09242010.txt
│   │       │   │       ├── speeches_09252015.txt
│   │       │   │       ├── speeches_09262000.txt
│   │       │   │       ├── speeches_09272005.txt
│   │       │   │       ├── speeches_09281995.txt
│   │       │   │       ├── speeches_10032005.txt
│   │       │   │       ├── speeches_10051985.txt
│   │       │   │       ├── speeches_10091985.txt
│   │       │   │       └── speeches_10121995.txt
│   │       │   ├── manual
│   │       │   │   ├── hein-bound
│   │       │   │   │   ├── 01101920.txt
│   │       │   │   │   ├── 01111900.txt
│   │       │   │   │   ├── 01111910.txt
│   │       │   │   │   ├── 01121950.txt
│   │       │   │   │   ├── 01131880.txt
│   │       │   │   │   ├── 01131930.txt
│   │       │   │   │   ├── 01161890.txt
│   │       │   │   │   ├── 01161940.txt
│   │       │   │   │   ├── 01181960.txt
│   │       │   │   │   ├── 01202010.txt
│   │       │   │   │   ├── 01231980.txt
│   │       │   │   │   ├── 01271970.txt
│   │       │   │   │   ├── 01311990.txt
│   │       │   │   │   ├── 02022000.txt
│   │       │   │   │   ├── 03301920.txt
│   │       │   │   │   ├── 03311900.txt
│   │       │   │   │   ├── 04051880.txt
│   │       │   │   │   ├── 04091910.txt
│   │       │   │   │   ├── 04171930.txt
│   │       │   │   │   ├── 05091900.txt
│   │       │   │   │   ├── 05101960.txt
│   │       │   │   │   ├── 05111920.txt
│   │       │   │   │   ├── 05131880.txt
│   │       │   │   │   ├── 05141900.txt
│   │       │   │   │   ├── 05151920.txt
│   │       │   │   │   ├── 05191880.txt
│   │       │   │   │   ├── 05191910.txt
│   │       │   │   │   ├── 05241910.txt
│   │       │   │   │   ├── 05261950.txt
│   │       │   │   │   ├── 05291890.txt
│   │       │   │   │   ├── 06021980.txt
│   │       │   │   │   ├── 06031940.txt
│   │       │   │   │   ├── 06101930.txt
│   │       │   │   │   ├── 06111990.txt
│   │       │   │   │   ├── 06141930.txt
│   │       │   │   │   ├── 06192000.txt
│   │       │   │   │   ├── 06221970.txt
│   │       │   │   │   ├── 06252010.txt
│   │       │   │   │   ├── 07051960.txt
│   │       │   │   │   ├── 07111960.txt
│   │       │   │   │   ├── 08031950.txt
│   │       │   │   │   ├── 08091890.txt
│   │       │   │   │   ├── 08101950.txt
│   │       │   │   │   ├── 08161890.txt
│   │       │   │   │   ├── 08221980.txt
│   │       │   │   │   ├── 08281980.txt
│   │       │   │   │   ├── 08301940.txt
│   │       │   │   │   ├── 08311970.txt
│   │       │   │   │   ├── 09061990.txt
│   │       │   │   │   ├── 09071940.txt
│   │       │   │   │   ├── 09101970.txt
│   │       │   │   │   ├── 09131990.txt
│   │       │   │   │   ├── 09212000.txt
│   │       │   │   │   ├── 09272000.txt
│   │       │   │   │   ├── 09272010.txt
│   │       │   │   │   └── 10012010.txt
│   │       │   │   └── hein-daily
│   │       │   │       ├── 01111995.txt
│   │       │   │       ├── 01132015.txt
│   │       │   │       ├── 01212010.txt
│   │       │   │       ├── 01291985.txt
│   │       │   │       ├── 01311990.txt
│   │       │   │       ├── 01312005.txt
│   │       │   │       ├── 02012000.txt
│   │       │   │       ├── 06092010.txt
│   │       │   │       ├── 06102015.txt
│   │       │   │       ├── 06121990.txt
│   │       │   │       ├── 06162000.txt
│   │       │   │       ├── 06212005.txt
│   │       │   │       ├── 06221995.txt
│   │       │   │       ├── 06271985.txt
│   │       │   │       ├── 09101990.txt
│   │       │   │       ├── 09141990.txt
│   │       │   │       ├── 09172015.txt
│   │       │   │       ├── 09202000.txt
│   │       │   │       ├── 09202010.txt
│   │       │   │       ├── 09242010.txt
│   │       │   │       ├── 09252015.txt
│   │       │   │       ├── 09262000.txt
│   │       │   │       ├── 09272005.txt
│   │       │   │       ├── 09281995.txt
│   │       │   │       ├── 10032005.txt
│   │       │   │       ├── 10051985.txt
│   │       │   │       ├── 10091985.txt
│   │       │   │       └── 10121995.txt
│   │       │   ├── raw
│   │       │   │   ├── hein-bound
│   │       │   │   │   ├── 01101920.txt
│   │       │   │   │   ├── 01111900.txt
│   │       │   │   │   ├── 01111910.txt
│   │       │   │   │   ├── 01121950.txt
│   │       │   │   │   ├── 01131880.txt
│   │       │   │   │   ├── 01131930.txt
│   │       │   │   │   ├── 01161890.txt
│   │       │   │   │   ├── 01161940.txt
│   │       │   │   │   ├── 01181960.txt
│   │       │   │   │   ├── 01202010.txt
│   │       │   │   │   ├── 01231980.txt
│   │       │   │   │   ├── 01271970.txt
│   │       │   │   │   ├── 01311990.txt
│   │       │   │   │   ├── 02022000.txt
│   │       │   │   │   ├── 03301920.txt
│   │       │   │   │   ├── 03311900.txt
│   │       │   │   │   ├── 04051880.txt
│   │       │   │   │   ├── 04091910.txt
│   │       │   │   │   ├── 04171930.txt
│   │       │   │   │   ├── 05091900.txt
│   │       │   │   │   ├── 05101960.txt
│   │       │   │   │   ├── 05111920.txt
│   │       │   │   │   ├── 05131880.txt
│   │       │   │   │   ├── 05141900.txt
│   │       │   │   │   ├── 05151920.txt
│   │       │   │   │   ├── 05191880.txt
│   │       │   │   │   ├── 05191910.txt
│   │       │   │   │   ├── 05241910.txt
│   │       │   │   │   ├── 05261950.txt
│   │       │   │   │   ├── 05291890.txt
│   │       │   │   │   ├── 06021980.txt
│   │       │   │   │   ├── 06031940.txt
│   │       │   │   │   ├── 06101930.txt
│   │       │   │   │   ├── 06111990.txt
│   │       │   │   │   ├── 06141930.txt
│   │       │   │   │   ├── 06192000.txt
│   │       │   │   │   ├── 06221970.txt
│   │       │   │   │   ├── 06252010.txt
│   │       │   │   │   ├── 07051960.txt
│   │       │   │   │   ├── 07111960.txt
│   │       │   │   │   ├── 08031950.txt
│   │       │   │   │   ├── 08091890.txt
│   │       │   │   │   ├── 08101950.txt
│   │       │   │   │   ├── 08161890.txt
│   │       │   │   │   ├── 08221980.txt
│   │       │   │   │   ├── 08281980.txt
│   │       │   │   │   ├── 08301940.txt
│   │       │   │   │   ├── 08311970.txt
│   │       │   │   │   ├── 09061990.txt
│   │       │   │   │   ├── 09071940.txt
│   │       │   │   │   ├── 09101970.txt
│   │       │   │   │   ├── 09131990.txt
│   │       │   │   │   ├── 09212000.txt
│   │       │   │   │   ├── 09272000.txt
│   │       │   │   │   ├── 09272010.txt
│   │       │   │   │   └── 10012010.txt
│   │       │   │   └── hein-daily
│   │       │   │       ├── 01111995.txt
│   │       │   │       ├── 01132015.txt
│   │       │   │       ├── 01212010.txt
│   │       │   │       ├── 01291985.txt
│   │       │   │       ├── 01311990.txt
│   │       │   │       ├── 01312005.txt
│   │       │   │       ├── 02012000.txt
│   │       │   │       ├── 06092010.txt
│   │       │   │       ├── 06102015.txt
│   │       │   │       ├── 06121990.txt
│   │       │   │       ├── 06162000.txt
│   │       │   │       ├── 06212005.txt
│   │       │   │       ├── 06221995.txt
│   │       │   │       ├── 06271985.txt
│   │       │   │       ├── 09101990.txt
│   │       │   │       ├── 09141990.txt
│   │       │   │       ├── 09172015.txt
│   │       │   │       ├── 09202000.txt
│   │       │   │       ├── 09202010.txt
│   │       │   │       ├── 09242010.txt
│   │       │   │       ├── 09252015.txt
│   │       │   │       ├── 09262000.txt
│   │       │   │       ├── 09272005.txt
│   │       │   │       ├── 09281995.txt
│   │       │   │       ├── 10032005.txt
│   │       │   │       ├── 10051985.txt
│   │       │   │       ├── 10091985.txt
│   │       │   │       └── 10121995.txt
│   │       │   ├── results
│   │       │   │   ├── hein-bound
│   │       │   │   │   ├── comparison_046.txt
│   │       │   │   │   ├── comparison_051.txt
│   │       │   │   │   ├── comparison_056.txt
│   │       │   │   │   ├── comparison_061.txt
│   │       │   │   │   ├── comparison_066.txt
│   │       │   │   │   ├── comparison_071.txt
│   │       │   │   │   ├── comparison_076.txt
│   │       │   │   │   ├── comparison_081.txt
│   │       │   │   │   ├── comparison_086.txt
│   │       │   │   │   ├── comparison_091.txt
│   │       │   │   │   ├── comparison_096.txt
│   │       │   │   │   ├── comparison_101.txt
│   │       │   │   │   ├── comparison_106.txt
│   │       │   │   │   ├── comparison_111.txt
│   │       │   │   │   ├── comparison_master.txt
│   │       │   │   │   ├── errors_046.txt
│   │       │   │   │   ├── errors_051.txt
│   │       │   │   │   ├── errors_056.txt
│   │       │   │   │   ├── errors_061.txt
│   │       │   │   │   ├── errors_066.txt
│   │       │   │   │   ├── errors_071.txt
│   │       │   │   │   ├── errors_076.txt
│   │       │   │   │   ├── errors_081.txt
│   │       │   │   │   ├── errors_086.txt
│   │       │   │   │   ├── errors_091.txt
│   │       │   │   │   ├── errors_096.txt
│   │       │   │   │   ├── errors_101.txt
│   │       │   │   │   ├── errors_106.txt
│   │       │   │   │   └── errors_111.txt
│   │       │   │   └── hein-daily
│   │       │   │       ├── comparison_099.txt
│   │       │   │       ├── comparison_101.txt
│   │       │   │       ├── comparison_104.txt
│   │       │   │       ├── comparison_106.txt
│   │       │   │       ├── comparison_109.txt
│   │       │   │       ├── comparison_111.txt
│   │       │   │       ├── comparison_114.txt
│   │       │   │       ├── comparison_master.txt
│   │       │   │       ├── errors_099.txt
│   │       │   │       ├── errors_101.txt
│   │       │   │       ├── errors_104.txt
│   │       │   │       ├── errors_106.txt
│   │       │   │       ├── errors_109.txt
│   │       │   │       ├── errors_111.txt
│   │       │   │       └── errors_114.txt
│   │       │   └── selection
│   │       │       ├── audit_selections-hein-bound.txt
│   │       │       └── audit_selections-hein-daily.txt
│   │       └── speakermap
│   │           ├── hein-bound_errors.txt
│   │           └── hein-daily_errors.txt
│   └── __MACOSX
│       └── audit
│           └── audit
│               ├── parsing
│               │   ├── auto
│               │   │   ├── hein-bound
│               │   │   └── hein-daily
│               │   ├── manual
│               │   │   ├── hein-bound
│               │   │   └── hein-daily
│               │   ├── raw
│               │   │   ├── hein-bound
│               │   │   └── hein-daily
│               │   ├── results
│               │   │   ├── hein-bound
│               │   │   └── hein-daily
│               │   └── selection
│               └── speakermap
├── hein-daily
│   ├── hein-daily
│   │   ├── 097_SpeakerMap.txt
│   │   ├── 098_SpeakerMap.txt
│   │   ├── 099_SpeakerMap.txt
│   │   ├── 100_SpeakerMap.txt
│   │   ├── 101_SpeakerMap.txt
│   │   ├── 102_SpeakerMap.txt
│   │   ├── 103_SpeakerMap.txt
│   │   ├── 104_SpeakerMap.txt
│   │   ├── 105_SpeakerMap.txt
│   │   ├── 106_SpeakerMap.txt
│   │   ├── 107_SpeakerMap.txt
│   │   ├── 108_SpeakerMap.txt
│   │   ├── 109_SpeakerMap.txt
│   │   ├── 110_SpeakerMap.txt
│   │   ├── 111_SpeakerMap.txt
│   │   ├── 112_SpeakerMap.txt
│   │   ├── 113_SpeakerMap.txt
│   │   ├── 114_SpeakerMap.txt
│   │   ├── byparty_2gram_097.txt
│   │   ├── byparty_2gram_098.txt
│   │   ├── byparty_2gram_099.txt
│   │   ├── byparty_2gram_100.txt
│   │   ├── byparty_2gram_101.txt
│   │   ├── byparty_2gram_102.txt
│   │   ├── byparty_2gram_103.txt
│   │   ├── byparty_2gram_104.txt
│   │   ├── byparty_2gram_105.txt
│   │   ├── byparty_2gram_106.txt
│   │   ├── byparty_2gram_107.txt
│   │   ├── byparty_2gram_108.txt
│   │   ├── byparty_2gram_109.txt
│   │   ├── byparty_2gram_110.txt
│   │   ├── byparty_2gram_111.txt
│   │   ├── byparty_2gram_112.txt
│   │   ├── byparty_2gram_113.txt
│   │   ├── byparty_2gram_114.txt
│   │   ├── byspeaker_2gram_097.txt
│   │   ├── byspeaker_2gram_098.txt
│   │   ├── byspeaker_2gram_099.txt
│   │   ├── byspeaker_2gram_100.txt
│   │   ├── byspeaker_2gram_101.txt
│   │   ├── byspeaker_2gram_102.txt
│   │   ├── byspeaker_2gram_103.txt
│   │   ├── byspeaker_2gram_104.txt
│   │   ├── byspeaker_2gram_105.txt
│   │   ├── byspeaker_2gram_106.txt
│   │   ├── byspeaker_2gram_107.txt
│   │   ├── byspeaker_2gram_108.txt
│   │   ├── byspeaker_2gram_109.txt
│   │   ├── byspeaker_2gram_110.txt
│   │   ├── byspeaker_2gram_111.txt
│   │   ├── byspeaker_2gram_112.txt
│   │   ├── byspeaker_2gram_113.txt
│   │   ├── byspeaker_2gram_114.txt
│   │   ├── descr_097.txt
│   │   ├── descr_098.txt
│   │   ├── descr_099.txt
│   │   ├── descr_100.txt
│   │   ├── descr_101.txt
│   │   ├── descr_102.txt
│   │   ├── descr_103.txt
│   │   ├── descr_104.txt
│   │   ├── descr_105.txt
│   │   ├── descr_106.txt
│   │   ├── descr_107.txt
│   │   ├── descr_108.txt
│   │   ├── descr_109.txt
│   │   ├── descr_110.txt
│   │   ├── descr_111.txt
│   │   ├── descr_112.txt
│   │   ├── descr_113.txt
│   │   ├── descr_114.txt
│   │   ├── speeches_097.txt
│   │   ├── speeches_098.txt
│   │   ├── speeches_099.txt
│   │   ├── speeches_100.txt
│   │   ├── speeches_101.txt
│   │   ├── speeches_102.txt
│   │   ├── speeches_103.txt
│   │   ├── speeches_104.txt
│   │   ├── speeches_105.txt
│   │   ├── speeches_106.txt
│   │   ├── speeches_107.txt
│   │   ├── speeches_108.txt
│   │   ├── speeches_109.txt
│   │   ├── speeches_110.txt
│   │   ├── speeches_111.txt
│   │   ├── speeches_112.txt
│   │   ├── speeches_113.txt
│   │   └── speeches_114.txt
│   └── __MACOSX
│       └── hein-daily
├── README.md
├── speakermap_stats
│   ├── __MACOSX
│   │   └── speakermap_stats
│   └── speakermap_stats
│       ├── hein-bound.txt
│       └── hein-daily.txt
└── vocabulary
    ├── __MACOSX
    │   └── vocabulary
    └── vocabulary
        ├── master_list.txt
        ├── procedural.txt
        └── vocab.txt
