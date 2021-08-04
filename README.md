# introduction:

The purpose of service is to analyze the mission and provide all relevant parameters
regarding mission(covered groves, survey, area, height...), customer, sensors, rigs, and splitter

#### - Endpoints: 
    /flightDiscover 
    dev_url: "https://ppk-manager-wdnusxy7na-uc.a.run.app"
    prod_url: "http://flight-discovery.default.example.com"


#### - input:
    the following json:

    {
    "locations":[{
            "ImageName": "12513_DSC06576.JPG",
            "lat": -23.5743022,
            "lon": -48.1908535,
            "z": 762.8,
            "yaw": 97.51,
            "pitch": -15.37,
            "roll": 5.89,
            "folderName": "12513"
	        },{
            "ImageName": "12513_DSC06577.JPG",
            "lat": -23.5742995,
            "lon": -48.1906731,
            "z": 761.35,
            "yaw": 99.25,
            "pitch": -10.32,
            "roll": 5.76,
            "folderName": "12513"
	}],
    
    "exif" : [{
            "ImageName": "12513_DSC06576.JPG",
            "DateTimeOriginal": "2015:02:05 01:03:57",
            "Make": "SONY",
            "Model": "ILCE-7RM2",
            "LensModel": "----",
            "ExifImageWidth": 7952,
            "ExifImageHeight": 5304,
            "FocalLength": 0,
            "Copyright": "a7r2_agr",
            "folderName": "12513",
            },{
            "ImageName": "12513_DSC06577.JPG",
            "DateTimeOriginal": "2015:02:05 01:03:59",
            "Make": "SONY",
            "Model": "ILCE-7RM2",
            "LensModel": "----",
            "ExifImageWidth": 7952,
            "ExifImageHeight": 5304,
            "FocalLength": 0,
            "Copyright": "a7r2_agr",
            "folderName": "12513"
    "gps": [
        {
            "ImageName": "12513_DSC06576.JPG",
            "utc": "2020:09:02 12:42:47",
            "lat": -23.5743022,
            "lon": -48.1908535,
            "height": 762.8,
            "folderName": "12513"
        },
        {
            "ImageName": "12513_DSC06577.JPG",
            "utc": "2020:09:02 12:42:49",
            "lat": -23.5742995,
            "lon": -48.1906731,
            "height": 761.35,
            "folderName": "12513"
    "mission_name": "itapetininga_200420201_120m_agr_1234_3453"
}

#### - Output

        {
    "sensors": [
        {
            "width": 3976,
            "height": 2652,
            "make": "sony",
            "model": "ilce-7rm2",
            "copyright": "a7r2_agr",
            "sensor_type": "agrowing",
            "sensorWidth": 17.9,
            "focal": 25.0
        }
    ],
    "Rig": {
        "sensors": [
            "a7r2_agr"
        ],
        "rig_name": "RIG_SONY_7RM2_AGRO"
    },
    "center": [
        -23.59913077261539,
        -48.328646704307715
    ],
    "bbox": [
        [
            -23.5966053,
            -48.322008700000005
        ],
        [
            -23.5966053,
            -48.333668599999996
        ],
        [
            -23.601190399999997,
            -48.322008700000005
        ],
        [
            -23.601190399999997,
            -48.333668599999996
        ]
    ],
    "region": {
        "measurementSystem": "metric",
        "name": "Brazil"
    },
    "IsMappingMission": true,
    "IsEvidence": false,
    "IsScoring": false,
    "MissionHeight": 116.69116469964747,
    "GeoObjects": {
        "data_acq": {
            "gsd": 2.101380128897072,
            "altitude": "116.69116469964747",
            "number_of_images": 325,
            "farm_name": "cs_itapetininga",
            "farmID": "-Low52WUjtgesf3YXjNG-dev",
            "splitter": {
                "threshold": 40,
                "grove_filter_type": 0
            },
            "mission_date": "2021-06-25",
            "survey_key": "-MbWlW_xxVOrvzmsRVSc",
            "customer_id": "-LyxJUeNlyl-JQfa3VE",
            "customer_name": "Citrosuco",
            "customer_survey_id": "-MY-LoJwZQlHi5LMWLsn",
            "customer_survey_name": "",
            "prev_survey_key": "-MQC40scnqYuu5s-XX1Y",
            "groves": [
                "-LowPcYTt7O1Qdys7ZXO",
                "-LowPdR61EefCtLH2KQa"
            ]
        },
        "splitter": {
            "groves": [
                {
                    "size_type": "MEDIUM",
                    "name": "monjolao-22101",
                    "groveID": "-LowPcYTt7O1Qdys7ZXO",
                    "index": "monjolao/22101",
                    "area": 7.7141992015733765,
                    "commodity": "Oranges",
                    "grove_output": {
                        "name": "monjolao-22101",
                        "groveID": "-LowPcYTt7O1Qdys7ZXO",
                        "number_of_files": "188",
                        "images_list": [
                            "DSC00185.JPG",
                            "DSC00186.JPG",
                            "DSC00187.JPG",
                            "DSC00188.JPG",
                            "DSC00189.JPG",
                            "DSC00190.JPG",
                            "DSC00191.JPG",
                            "DSC00192.JPG",
                            "DSC00193.JPG",
                            "DSC00194.JPG",
                            "DSC00195.JPG",
                            "DSC00196.JPG",
                            "DSC00197.JPG",
                            "DSC00198.JPG",
                            "DSC00199.JPG",
                            "DSC00200.JPG",
                            "DSC00201.JPG",
                            "DSC00202.JPG",
                            "DSC00203.JPG",
                            "DSC00204.JPG",
                            "DSC00205.JPG",
                            "DSC00206.JPG",
                            "DSC00207.JPG",
                            "DSC00208.JPG",
                            "DSC00209.JPG",
                            "DSC00210.JPG",
                            "DSC00211.JPG",
                            "DSC00212.JPG",
                            "DSC00213.JPG",
                            "DSC00214.JPG",
                            "DSC00215.JPG",
                            "DSC00216.JPG",
                            "DSC00217.JPG",
                            "DSC00218.JPG",
                            "DSC00219.JPG",
                            "DSC00220.JPG",
                            "DSC00221.JPG",
                            "DSC00222.JPG",
                            "DSC00223.JPG",
                            "DSC00224.JPG",
                            "DSC00225.JPG",
                            "DSC00226.JPG",
                            "DSC00227.JPG",
                            "DSC00228.JPG",
                            "DSC00229.JPG",
                            "DSC00230.JPG",
                            "DSC00231.JPG",
                            "DSC00232.JPG",
                            "DSC00233.JPG",
                            "DSC00234.JPG",
                            "DSC00235.JPG",
                            "DSC00236.JPG",
                            "DSC00237.JPG",
                            "DSC00238.JPG",
                            "DSC00239.JPG",
                            "DSC00240.JPG",
                            "DSC00241.JPG",
                            "DSC00242.JPG",
                            "DSC00243.JPG",
                            "DSC00244.JPG",
                            "DSC00245.JPG",
                            "DSC00246.JPG",
                            "DSC00247.JPG",
                            "DSC00248.JPG",
                            "DSC00249.JPG",
                            "DSC00250.JPG",
                            "DSC00251.JPG",
                            "DSC00252.JPG",
                            "DSC00253.JPG",
                            "DSC00254.JPG",
                            "DSC00255.JPG",
                            "DSC00256.JPG",
                            "DSC00257.JPG",
                            "DSC00258.JPG",
                            "DSC00259.JPG",
                            "DSC00260.JPG",
                            "DSC00261.JPG",
                            "DSC00262.JPG",
                            "DSC00263.JPG",
                            "DSC00264.JPG",
                            "DSC00265.JPG",
                            "DSC00266.JPG",
                            "DSC00267.JPG",
                            "DSC00268.JPG",
                            "DSC00269.JPG",
                            "DSC00270.JPG",
                            "DSC00271.JPG",
                            "DSC00272.JPG",
                            "DSC00273.JPG",
                            "DSC00274.JPG",
                            "DSC00275.JPG",
                            "DSC00276.JPG",
                            "DSC00277.JPG",
                            "DSC00278.JPG",
                            "DSC00279.JPG",
                            "DSC00280.JPG",
                            "DSC00281.JPG",
                            "DSC00282.JPG",
                            "DSC00283.JPG",
                            "DSC00284.JPG",
                            "DSC00285.JPG",
                            "DSC00286.JPG",
                            "DSC00287.JPG",
                            "DSC00288.JPG",
                            "DSC00289.JPG",
                            "DSC00290.JPG",
                            "DSC00291.JPG",
                            "DSC00292.JPG",
                            "DSC00293.JPG",
                            "DSC00294.JPG",
                            "DSC00295.JPG",
                            "DSC00296.JPG",
                            "DSC00297.JPG",
                            "DSC00298.JPG",
                            "DSC00299.JPG",
                            "DSC00300.JPG",
                            "DSC00301.JPG",
                            "DSC00302.JPG",
                            "DSC00303.JPG",
                            "DSC00304.JPG",
                            "DSC00305.JPG",
                            "DSC00306.JPG",
                            "DSC00307.JPG",
                            "DSC00308.JPG",
                            "DSC00309.JPG",
                            "DSC00310.JPG",
                            "DSC00311.JPG",
                            "DSC00312.JPG",
                            "DSC00313.JPG",
                            "DSC00314.JPG",
                            "DSC00315.JPG",
                            "DSC00316.JPG",
                            "DSC00317.JPG",
                            "DSC00318.JPG",
                            "DSC00319.JPG",
                            "DSC00320.JPG",
                            "DSC00321.JPG",
                            "DSC00322.JPG",
                            "DSC00323.JPG",
                            "DSC00324.JPG",
                            "DSC00325.JPG",
                            "DSC00326.JPG",
                            "DSC00327.JPG",
                            "DSC00328.JPG",
                            "DSC00329.JPG",
                            "DSC00330.JPG",
                            "DSC00331.JPG",
                            "DSC00332.JPG",
                            "DSC00333.JPG",
                            "DSC00334.JPG",
                            "DSC00335.JPG",
                            "DSC00336.JPG",
                            "DSC00337.JPG",
                            "DSC00338.JPG",
                            "DSC00339.JPG",
                            "DSC00340.JPG",
                            "DSC00341.JPG",
                            "DSC00342.JPG",
                            "DSC00343.JPG",
                            "DSC00344.JPG",
                            "DSC00345.JPG",
                            "DSC00346.JPG",
                            "DSC00347.JPG",
                            "DSC00348.JPG",
                            "DSC00349.JPG",
                            "DSC00350.JPG",
                            "DSC00351.JPG",
                            "DSC00352.JPG",
                            "DSC00353.JPG",
                            "DSC00354.JPG",
                            "DSC00355.JPG",
                            "DSC00356.JPG",
                            "DSC00357.JPG",
                            "DSC00358.JPG",
                            "DSC00359.JPG",
                            "DSC00360.JPG",
                            "DSC00361.JPG",
                            "DSC00362.JPG",
                            "DSC00363.JPG",
                            "DSC00364.JPG",
                            "DSC00365.JPG",
                            "DSC00366.JPG",
                            "DSC00367.JPG",
                            "DSC00368.JPG",
                            "DSC00369.JPG",
                            "DSC00370.JPG",
                            "DSC00371.JPG",
                            "DSC00372.JPG"
                        ],
                        "splitter_location": [
                            {
                                "ImageName": "DSC00185.JPG",
                                "lat": -23.598220899999998,
                                "lon": -48.329982,
                                "pitch": 3.59,
                                "roll": -0.39,
                                "yaw": 277.28,
                                "z": 725.78
                            },
                            {
                                "ImageName": "DSC00186.JPG",
                                "lat": -23.5983406,
                                "lon": -48.3301173,
                                "pitch": -8.82,
                                "roll": 0.99,
                                "yaw": 225.78,
                                "z": 725.08
                            },
                            {
                                "ImageName": "DSC00187.JPG",
                                "lat": -23.5984508,
                                "lon": -48.330241,
                                "pitch": -6.56,
                                "roll": 1.21,
                                "yaw": 225.96,
                                "z": 724.54
                            },
                            {
                                "ImageName": "DSC00188.JPG",
                                "lat": -23.598564899999996,
                                "lon": -48.3303695,
                                "pitch": -6.02,
                                "roll": 0.87,
                                "yaw": 225.4,
                                "z": 724.21
                            },
                            {
                                "ImageName": "DSC00189.JPG",
                                "lat": -23.598673100000003,
                                "lon": -48.3304911,
                                "pitch": -6.84,
                                "roll": 0.99,
                                "yaw": 225.62,
                                "z": 724.39
                            },
                            {
                                "ImageName": "DSC00190.JPG",
                                "lat": -23.5987814,
                                "lon": -48.3306125,
                                "pitch": -6.67,
                                "roll": 0.84,
                                "yaw": 225.59,
                                "z": 724.73
                            },
                            {
                                "ImageName": "DSC00191.JPG",
                                "lat": -23.598891300000002,
                                "lon": -48.3307361,
                                "pitch": -6.75,
                                "roll": 0.76,
                                "yaw": 225.63,
                                "z": 725.11
                            },
                            {
                                "ImageName": "DSC00192.JPG",
                                "lat": -23.598998,
                                "lon": -48.330856,
                                "pitch": -6.62,
                                "roll": 0.77,
                                "yaw": 225.49,
                                "z": 725.54
                            },
                            {
                                "ImageName": "DSC00193.JPG",
                                "lat": -23.599111699999998,
                                "lon": -48.330983700000004,
                                "pitch": -6.77,
                                "roll": 0.46,
                                "yaw": 225.65,
                                "z": 726.1
                            },
                            {
                                "ImageName": "DSC00194.JPG",
                                "lat": -23.5992224,
                                "lon": -48.331107700000004,
                                "pitch": -7.3,
                                "roll": 0.56,
                                "yaw": 225.69,
                                "z": 726.68
                            },
                            {
                                "ImageName": "DSC00195.JPG",
                                "lat": -23.599326,
                                "lon": -48.3312242,
                                "pitch": -7.04,
                                "roll": 0.31,
                                "yaw": 225.66,
                                "z": 727.29
                            },
                            {
                                "ImageName": "DSC00196.JPG",
                                "lat": -23.599435699999997,
                                "lon": -48.3313471,
                                "pitch": -7.18,
                                "roll": 0.5,
                                "yaw": 225.7,
                                "z": 727.91
                            },
                            {
                                "ImageName": "DSC00197.JPG",
                                "lat": -23.5995447,
                                "lon": -48.3314691,
                                "pitch": -7.19,
                                "roll": 0.59,
                                "yaw": 225.56,
                                "z": 728.17
                            },
                            {
                                "ImageName": "DSC00198.JPG",
                                "lat": -23.5996531,
                                "lon": -48.3315908,
                                "pitch": -7.14,
                                "roll": 0.48,
                                "yaw": 225.56,
                                "z": 728.32
                            },
                            {
                                "ImageName": "DSC00199.JPG",
                                "lat": -23.5997625,
                                "lon": -48.3317132,
                                "pitch": -7.05,
                                "roll": 0.71,
                                "yaw": 225.79,
                                "z": 728.51
                            },
                            {
                                "ImageName": "DSC00200.JPG",
                                "lat": -23.599874399999997,
                                "lon": -48.3318388,
                                "pitch": -6.97,
                                "roll": 0.58,
                                "yaw": 225.7,
                                "z": 728.81
                            },
                            {
                                "ImageName": "DSC00201.JPG",
                                "lat": -23.5999841,
                                "lon": -48.3319619,
                                "pitch": -7.06,
                                "roll": 0.52,
                                "yaw": 225.79,
                                "z": 729.16
                            },
                            {
                                "ImageName": "DSC00202.JPG",
                                "lat": -23.6000945,
                                "lon": -48.3320855,
                                "pitch": -7.05,
                                "roll": 0.64,
                                "yaw": 225.89,
                                "z": 729.62
                            },
                            {
                                "ImageName": "DSC00203.JPG",
                                "lat": -23.600206,
                                "lon": -48.3322106,
                                "pitch": -6.66,
                                "roll": 0.77,
                                "yaw": 225.99,
                                "z": 730.24
                            },
                            {
                                "ImageName": "DSC00204.JPG",
                                "lat": -23.600317699999998,
                                "lon": -48.3323357,
                                "pitch": -6.63,
                                "roll": 0.59,
                                "yaw": 225.7,
                                "z": 730.87
                            },
                            {
                                "ImageName": "DSC00205.JPG",
                                "lat": -23.600429000000002,
                                "lon": -48.33246,
                                "pitch": -7.09,
                                "roll": 1.01,
                                "yaw": 226.15,
                                "z": 731.41
                            },
                            {
                                "ImageName": "DSC00206.JPG",
                                "lat": -23.600539899999998,
                                "lon": -48.3325842,
                                "pitch": -6.7,
                                "roll": 1.18,
                                "yaw": 226.33,
                                "z": 731.75
                            },
                            {
                                "ImageName": "DSC00207.JPG",
                                "lat": -23.600651899999995,
                                "lon": -48.332710600000006,
                                "pitch": -6.81,
                                "roll": 0.9,
                                "yaw": 225.87,
                                "z": 731.97
                            },
                            {
                                "ImageName": "DSC00208.JPG",
                                "lat": -23.6007625,
                                "lon": -48.332835100000004,
                                "pitch": -6.8,
                                "roll": 0.5,
                                "yaw": 225.57,
                                "z": 731.93
                            },
                            {
                                "ImageName": "DSC00209.JPG",
                                "lat": -23.6008744,
                                "lon": -48.332960799999995,
                                "pitch": -5.62,
                                "roll": 0.64,
                                "yaw": 225.69,
                                "z": 731.76
                            },
                            {
                                "ImageName": "DSC00210.JPG",
                                "lat": -23.6009816,
                                "lon": -48.3330809,
                                "pitch": -2.76,
                                "roll": 0.53,
                                "yaw": 225.57,
                                "z": 731.37
                            },
                            {
                                "ImageName": "DSC00211.JPG",
                                "lat": -23.601088,
                                "lon": -48.3332,
                                "pitch": 2.34,
                                "roll": 0.69,
                                "yaw": 225.65,
                                "z": 730.74
                            },
                            {
                                "ImageName": "DSC00212.JPG",
                                "lat": -23.601190399999997,
                                "lon": -48.3333145,
                                "pitch": 3.07,
                                "roll": 0.86,
                                "yaw": 226.04,
                                "z": 730.04
                            },
                            {
                                "ImageName": "DSC00213.JPG",
                                "lat": -23.6009267,
                                "lon": -48.3335049,
                                "pitch": 2.69,
                                "roll": 3.94,
                                "yaw": 358.51,
                                "z": 730.22
                            },
                            {
                                "ImageName": "DSC00214.JPG",
                                "lat": -23.600811399999998,
                                "lon": -48.333371299999996,
                                "pitch": -8.52,
                                "roll": 0.94,
                                "yaw": 44.43,
                                "z": 730.59
                            },
                            {
                                "ImageName": "DSC00215.JPG",
                                "lat": -23.600700500000002,
                                "lon": -48.3332494,
                                "pitch": -7.26,
                                "roll": 1.14,
                                "yaw": 45.28,
                                "z": 731.15
                            },
                            {
                                "ImageName": "DSC00216.JPG",
                                "lat": -23.6005867,
                                "lon": -48.3331244,
                                "pitch": -6.82,
                                "roll": 1.38,
                                "yaw": 45.6,
                                "z": 731.71
                            },
                            {
                                "ImageName": "DSC00217.JPG",
                                "lat": -23.6004783,
                                "lon": -48.3330044,
                                "pitch": -7.01,
                                "roll": 1.33,
                                "yaw": 45.84,
                                "z": 731.95
                            },
                            {
                                "ImageName": "DSC00218.JPG",
                                "lat": -23.6003652,
                                "lon": -48.3328777,
                                "pitch": -6.89,
                                "roll": 0.88,
                                "yaw": 45.69,
                                "z": 732.01
                            },
                            {
                                "ImageName": "DSC00219.JPG",
                                "lat": -23.6002556,
                                "lon": -48.3327541,
                                "pitch": -6.95,
                                "roll": 0.51,
                                "yaw": 45.31,
                                "z": 731.96
                            },
                            {
                                "ImageName": "DSC00220.JPG",
                                "lat": -23.6001435,
                                "lon": -48.332629299999994,
                                "pitch": -6.66,
                                "roll": 0.85,
                                "yaw": 45.38,
                                "z": 731.51
                            },
                            {
                                "ImageName": "DSC00221.JPG",
                                "lat": -23.6000371,
                                "lon": -48.3325114,
                                "pitch": -6.94,
                                "roll": 1.26,
                                "yaw": 45.93,
                                "z": 730.69
                            },
                            {
                                "ImageName": "DSC00222.JPG",
                                "lat": -23.5999231,
                                "lon": -48.3323834,
                                "pitch": -6.77,
                                "roll": 0.83,
                                "yaw": 45.79,
                                "z": 729.81
                            },
                            {
                                "ImageName": "DSC00223.JPG",
                                "lat": -23.599819,
                                "lon": -48.3322664,
                                "pitch": -6.4,
                                "roll": 0.88,
                                "yaw": 45.98,
                                "z": 728.97
                            },
                            {
                                "ImageName": "DSC00224.JPG",
                                "lat": -23.5997098,
                                "lon": -48.3321435,
                                "pitch": -6.79,
                                "roll": 0.76,
                                "yaw": 45.67,
                                "z": 728.37
                            },
                            {
                                "ImageName": "DSC00225.JPG",
                                "lat": -23.5996008,
                                "lon": -48.3320215,
                                "pitch": -7.15,
                                "roll": 1.11,
                                "yaw": 46.0,
                                "z": 727.9
                            },
                            {
                                "ImageName": "DSC00226.JPG",
                                "lat": -23.5994932,
                                "lon": -48.3319011,
                                "pitch": -7.07,
                                "roll": 1.21,
                                "yaw": 46.11,
                                "z": 727.55
                            },
                            {
                                "ImageName": "DSC00227.JPG",
                                "lat": -23.5993815,
                                "lon": -48.3317759,
                                "pitch": -6.82,
                                "roll": 1.32,
                                "yaw": 46.05,
                                "z": 727.28
                            },
                            {
                                "ImageName": "DSC00228.JPG",
                                "lat": -23.599270800000003,
                                "lon": -48.3316515,
                                "pitch": -6.78,
                                "roll": 1.04,
                                "yaw": 46.02,
                                "z": 727.06
                            },
                            {
                                "ImageName": "DSC00229.JPG",
                                "lat": -23.599162699999997,
                                "lon": -48.3315299,
                                "pitch": -6.95,
                                "roll": 1.1,
                                "yaw": 45.88,
                                "z": 726.85
                            },
                            {
                                "ImageName": "DSC00230.JPG",
                                "lat": -23.599051199999998,
                                "lon": -48.3314047,
                                "pitch": -7.04,
                                "roll": 1.04,
                                "yaw": 45.81,
                                "z": 726.66
                            },
                            {
                                "ImageName": "DSC00231.JPG",
                                "lat": -23.598938600000004,
                                "lon": -48.3312783,
                                "pitch": -7.19,
                                "roll": 1.08,
                                "yaw": 45.78,
                                "z": 726.35
                            },
                            {
                                "ImageName": "DSC00232.JPG",
                                "lat": -23.5988294,
                                "lon": -48.331155700000004,
                                "pitch": -7.23,
                                "roll": 0.95,
                                "yaw": 45.67,
                                "z": 725.83
                            },
                            {
                                "ImageName": "DSC00233.JPG",
                                "lat": -23.5987161,
                                "lon": -48.3310282,
                                "pitch": -7.1,
                                "roll": 0.7,
                                "yaw": 45.68,
                                "z": 725.28
                            },
                            {
                                "ImageName": "DSC00234.JPG",
                                "lat": -23.5986043,
                                "lon": -48.3309029,
                                "pitch": -7.01,
                                "roll": 0.83,
                                "yaw": 45.6,
                                "z": 724.77
                            },
                            {
                                "ImageName": "DSC00235.JPG",
                                "lat": -23.5984935,
                                "lon": -48.3307789,
                                "pitch": -7.29,
                                "roll": 0.93,
                                "yaw": 45.71,
                                "z": 724.36
                            },
                            {
                                "ImageName": "DSC00236.JPG",
                                "lat": -23.5983827,
                                "lon": -48.3306548,
                                "pitch": -5.6,
                                "roll": 0.73,
                                "yaw": 45.58,
                                "z": 724.06
                            },
                            {
                                "ImageName": "DSC00237.JPG",
                                "lat": -23.598275,
                                "lon": -48.3305343,
                                "pitch": -3.03,
                                "roll": 0.89,
                                "yaw": 45.79,
                                "z": 724.08
                            },
                            {
                                "ImageName": "DSC00238.JPG",
                                "lat": -23.5981677,
                                "lon": -48.33041420000001,
                                "pitch": 1.67,
                                "roll": 0.79,
                                "yaw": 45.92,
                                "z": 724.3
                            },
                            {
                                "ImageName": "DSC00239.JPG",
                                "lat": -23.5980667,
                                "lon": -48.33030120000001,
                                "pitch": 3.29,
                                "roll": 0.42,
                                "yaw": 45.67,
                                "z": 724.73
                            },
                            {
                                "ImageName": "DSC00240.JPG",
                                "lat": -23.5978183,
                                "lon": -48.330503799999995,
                                "pitch": 5.2,
                                "roll": 1.14,
                                "yaw": 299.38,
                                "z": 724.87
                            },
                            {
                                "ImageName": "DSC00241.JPG",
                                "lat": -23.5979391,
                                "lon": -48.330639700000006,
                                "pitch": -8.92,
                                "roll": 1.25,
                                "yaw": 226.12,
                                "z": 724.35
                            },
                            {
                                "ImageName": "DSC00242.JPG",
                                "lat": -23.5980502,
                                "lon": -48.3307657,
                                "pitch": -6.48,
                                "roll": 0.9,
                                "yaw": 225.59,
                                "z": 723.93
                            },
                            {
                                "ImageName": "DSC00243.JPG",
                                "lat": -23.5981629,
                                "lon": -48.330892799999994,
                                "pitch": -6.53,
                                "roll": 0.7,
                                "yaw": 225.29,
                                "z": 723.7
                            },
                            {
                                "ImageName": "DSC00244.JPG",
                                "lat": -23.598270199999998,
                                "lon": -48.3310135,
                                "pitch": -6.88,
                                "roll": 0.69,
                                "yaw": 225.35,
                                "z": 723.68
                            },
                            {
                                "ImageName": "DSC00245.JPG",
                                "lat": -23.5983838,
                                "lon": -48.3311409,
                                "pitch": -6.96,
                                "roll": 0.8,
                                "yaw": 225.56,
                                "z": 723.74
                            },
                            {
                                "ImageName": "DSC00246.JPG",
                                "lat": -23.598494199999998,
                                "lon": -48.3312646,
                                "pitch": -7.35,
                                "roll": 0.81,
                                "yaw": 225.76,
                                "z": 723.98
                            },
                            {
                                "ImageName": "DSC00247.JPG",
                                "lat": -23.598600100000002,
                                "lon": -48.3313836,
                                "pitch": -7.74,
                                "roll": 0.91,
                                "yaw": 225.47,
                                "z": 724.37
                            },
                            {
                                "ImageName": "DSC00248.JPG",
                                "lat": -23.5987139,
                                "lon": -48.331512,
                                "pitch": -7.2,
                                "roll": 0.59,
                                "yaw": 225.61,
                                "z": 724.65
                            },
                            {
                                "ImageName": "DSC00249.JPG",
                                "lat": -23.5988253,
                                "lon": -48.331636700000004,
                                "pitch": -6.85,
                                "roll": 0.68,
                                "yaw": 225.52,
                                "z": 724.87
                            },
                            {
                                "ImageName": "DSC00250.JPG",
                                "lat": -23.598929100000003,
                                "lon": -48.3317528,
                                "pitch": -7.17,
                                "roll": 0.64,
                                "yaw": 225.65,
                                "z": 725.11
                            },
                            {
                                "ImageName": "DSC00251.JPG",
                                "lat": -23.5990389,
                                "lon": -48.3318761,
                                "pitch": -7.09,
                                "roll": 0.56,
                                "yaw": 225.41,
                                "z": 725.39
                            },
                            {
                                "ImageName": "DSC00252.JPG",
                                "lat": -23.5991457,
                                "lon": -48.3319958,
                                "pitch": -6.84,
                                "roll": 0.67,
                                "yaw": 225.8,
                                "z": 725.59
                            },
                            {
                                "ImageName": "DSC00253.JPG",
                                "lat": -23.599255600000003,
                                "lon": -48.332118799999996,
                                "pitch": -7.32,
                                "roll": 0.71,
                                "yaw": 225.88,
                                "z": 725.8
                            },
                            {
                                "ImageName": "DSC00254.JPG",
                                "lat": -23.5993673,
                                "lon": -48.33224370000001,
                                "pitch": -7.28,
                                "roll": 0.96,
                                "yaw": 225.93,
                                "z": 726.05
                            },
                            {
                                "ImageName": "DSC00255.JPG",
                                "lat": -23.599474899999997,
                                "lon": -48.3323648,
                                "pitch": -7.76,
                                "roll": 0.43,
                                "yaw": 225.7,
                                "z": 726.45
                            },
                            {
                                "ImageName": "DSC00256.JPG",
                                "lat": -23.599586600000002,
                                "lon": -48.3324907,
                                "pitch": -7.47,
                                "roll": 0.17,
                                "yaw": 225.74,
                                "z": 727.29
                            },
                            {
                                "ImageName": "DSC00257.JPG",
                                "lat": -23.5996974,
                                "lon": -48.3326152,
                                "pitch": -6.99,
                                "roll": 0.3,
                                "yaw": 225.75,
                                "z": 728.17
                            },
                            {
                                "ImageName": "DSC00258.JPG",
                                "lat": -23.599806899999997,
                                "lon": -48.3327376,
                                "pitch": -7.29,
                                "roll": 0.45,
                                "yaw": 225.69,
                                "z": 729.05
                            },
                            {
                                "ImageName": "DSC00259.JPG",
                                "lat": -23.5999174,
                                "lon": -48.3328611,
                                "pitch": -7.34,
                                "roll": 0.59,
                                "yaw": 225.93,
                                "z": 729.91
                            },
                            {
                                "ImageName": "DSC00260.JPG",
                                "lat": -23.6000267,
                                "lon": -48.332983500000005,
                                "pitch": -7.53,
                                "roll": 0.41,
                                "yaw": 226.03,
                                "z": 730.76
                            },
                            {
                                "ImageName": "DSC00261.JPG",
                                "lat": -23.6001372,
                                "lon": -48.3331078,
                                "pitch": -7.56,
                                "roll": 0.3,
                                "yaw": 226.15,
                                "z": 731.6
                            },
                            {
                                "ImageName": "DSC00262.JPG",
                                "lat": -23.6002467,
                                "lon": -48.33323,
                                "pitch": -5.92,
                                "roll": 0.66,
                                "yaw": 225.63,
                                "z": 732.33
                            },
                            {
                                "ImageName": "DSC00263.JPG",
                                "lat": -23.600356,
                                "lon": -48.333351799999996,
                                "pitch": -0.77,
                                "roll": 1.11,
                                "yaw": 225.87,
                                "z": 732.56
                            },
                            {
                                "ImageName": "DSC00264.JPG",
                                "lat": -23.6004573,
                                "lon": -48.3334644,
                                "pitch": 2.39,
                                "roll": 1.52,
                                "yaw": 226.23,
                                "z": 731.74
                            },
                            {
                                "ImageName": "DSC00265.JPG",
                                "lat": -23.600557199999997,
                                "lon": -48.33357879999999,
                                "pitch": 5.88,
                                "roll": 0.91,
                                "yaw": 227.81,
                                "z": 730.93
                            },
                            {
                                "ImageName": "DSC00266.JPG",
                                "lat": -23.599929,
                                "lon": -48.3333596,
                                "pitch": 0.81,
                                "roll": 2.06,
                                "yaw": 24.73,
                                "z": 731.46
                            },
                            {
                                "ImageName": "DSC00267.JPG",
                                "lat": -23.5998122,
                                "lon": -48.3332255,
                                "pitch": -8.94,
                                "roll": 0.92,
                                "yaw": 45.21,
                                "z": 731.04
                            },
                            {
                                "ImageName": "DSC00268.JPG",
                                "lat": -23.5997004,
                                "lon": -48.3331015,
                                "pitch": -6.95,
                                "roll": 1.07,
                                "yaw": 45.54,
                                "z": 730.29
                            },
                            {
                                "ImageName": "DSC00269.JPG",
                                "lat": -23.5995855,
                                "lon": -48.3329756,
                                "pitch": -6.89,
                                "roll": 1.56,
                                "yaw": 46.07,
                                "z": 729.48
                            },
                            {
                                "ImageName": "DSC00270.JPG",
                                "lat": -23.599476899999996,
                                "lon": -48.332854499999996,
                                "pitch": -6.45,
                                "roll": 1.02,
                                "yaw": 45.88,
                                "z": 728.66
                            },
                            {
                                "ImageName": "DSC00271.JPG",
                                "lat": -23.5993684,
                                "lon": -48.3327331,
                                "pitch": -6.87,
                                "roll": 1.13,
                                "yaw": 45.66,
                                "z": 727.78
                            },
                            {
                                "ImageName": "DSC00272.JPG",
                                "lat": -23.5992568,
                                "lon": -48.3326078,
                                "pitch": -6.41,
                                "roll": 0.72,
                                "yaw": 45.76,
                                "z": 726.85
                            },
                            {
                                "ImageName": "DSC00273.JPG",
                                "lat": -23.5991516,
                                "lon": -48.3324898,
                                "pitch": -6.24,
                                "roll": 0.58,
                                "yaw": 45.38,
                                "z": 725.94
                            },
                            {
                                "ImageName": "DSC00274.JPG",
                                "lat": -23.599038399999998,
                                "lon": -48.332363,
                                "pitch": -6.26,
                                "roll": 0.36,
                                "yaw": 45.37,
                                "z": 725.06
                            },
                            {
                                "ImageName": "DSC00275.JPG",
                                "lat": -23.598926199999998,
                                "lon": -48.332237400000004,
                                "pitch": -6.05,
                                "roll": 0.47,
                                "yaw": 45.63,
                                "z": 724.44
                            },
                            {
                                "ImageName": "DSC00276.JPG",
                                "lat": -23.5988114,
                                "lon": -48.332109100000004,
                                "pitch": -6.07,
                                "roll": 0.71,
                                "yaw": 45.68,
                                "z": 724.16
                            },
                            {
                                "ImageName": "DSC00277.JPG",
                                "lat": -23.5987077,
                                "lon": -48.33199329999999,
                                "pitch": -6.65,
                                "roll": 0.9,
                                "yaw": 45.8,
                                "z": 723.92
                            },
                            {
                                "ImageName": "DSC00278.JPG",
                                "lat": -23.5986006,
                                "lon": -48.3318736,
                                "pitch": -6.9,
                                "roll": 1.11,
                                "yaw": 46.16,
                                "z": 723.66
                            },
                            {
                                "ImageName": "DSC00279.JPG",
                                "lat": -23.5984861,
                                "lon": -48.3317447,
                                "pitch": -6.98,
                                "roll": 0.87,
                                "yaw": 45.94,
                                "z": 723.39
                            },
                            {
                                "ImageName": "DSC00280.JPG",
                                "lat": -23.5983794,
                                "lon": -48.331625,
                                "pitch": -6.81,
                                "roll": 1.01,
                                "yaw": 46.0,
                                "z": 723.17
                            },
                            {
                                "ImageName": "DSC00281.JPG",
                                "lat": -23.598271899999997,
                                "lon": -48.3315039,
                                "pitch": -7.1,
                                "roll": 0.86,
                                "yaw": 45.78,
                                "z": 723.03
                            },
                            {
                                "ImageName": "DSC00282.JPG",
                                "lat": -23.598160399999998,
                                "lon": -48.3313787,
                                "pitch": -6.82,
                                "roll": 0.97,
                                "yaw": 46.17,
                                "z": 722.91
                            },
                            {
                                "ImageName": "DSC00283.JPG",
                                "lat": -23.598048100000003,
                                "lon": -48.331252899999996,
                                "pitch": -7.15,
                                "roll": 1.03,
                                "yaw": 46.19,
                                "z": 722.82
                            },
                            {
                                "ImageName": "DSC00284.JPG",
                                "lat": -23.5979384,
                                "lon": -48.331129499999996,
                                "pitch": -4.64,
                                "roll": 0.88,
                                "yaw": 45.89,
                                "z": 722.83
                            },
                            {
                                "ImageName": "DSC00285.JPG",
                                "lat": -23.5978295,
                                "lon": -48.331007899999996,
                                "pitch": -0.99,
                                "roll": 1.26,
                                "yaw": 46.11,
                                "z": 722.91
                            },
                            {
                                "ImageName": "DSC00286.JPG",
                                "lat": -23.5977226,
                                "lon": -48.3308901,
                                "pitch": 2.21,
                                "roll": 1.81,
                                "yaw": 46.84,
                                "z": 723.18
                            },
                            {
                                "ImageName": "DSC00287.JPG",
                                "lat": -23.597625,
                                "lon": -48.3307784,
                                "pitch": 4.45,
                                "roll": 1.59,
                                "yaw": 49.38,
                                "z": 723.85
                            },
                            {
                                "ImageName": "DSC00288.JPG",
                                "lat": -23.5974139,
                                "lon": -48.3310247,
                                "pitch": 4.98,
                                "roll": 0.42,
                                "yaw": 299.05,
                                "z": 722.7
                            },
                            {
                                "ImageName": "DSC00289.JPG",
                                "lat": -23.5975313,
                                "lon": -48.3311553,
                                "pitch": -9.39,
                                "roll": 1.16,
                                "yaw": 225.75,
                                "z": 721.99
                            },
                            {
                                "ImageName": "DSC00290.JPG",
                                "lat": -23.597642999999998,
                                "lon": -48.33128189999999,
                                "pitch": -7.18,
                                "roll": 0.8,
                                "yaw": 224.93,
                                "z": 721.61
                            },
                            {
                                "ImageName": "DSC00291.JPG",
                                "lat": -23.597755300000003,
                                "lon": -48.3314071,
                                "pitch": -7.16,
                                "roll": 0.98,
                                "yaw": 225.51,
                                "z": 721.39
                            },
                            {
                                "ImageName": "DSC00292.JPG",
                                "lat": -23.5978638,
                                "lon": -48.331528799999994,
                                "pitch": -7.16,
                                "roll": 0.85,
                                "yaw": 225.62,
                                "z": 721.54
                            },
                            {
                                "ImageName": "DSC00293.JPG",
                                "lat": -23.5979725,
                                "lon": -48.331651,
                                "pitch": -7.04,
                                "roll": 0.8,
                                "yaw": 225.65,
                                "z": 721.64
                            },
                            {
                                "ImageName": "DSC00294.JPG",
                                "lat": -23.5980853,
                                "lon": -48.3317785,
                                "pitch": -6.6,
                                "roll": 0.61,
                                "yaw": 225.48,
                                "z": 721.8
                            },
                            {
                                "ImageName": "DSC00295.JPG",
                                "lat": -23.598193600000002,
                                "lon": -48.3319001,
                                "pitch": -7.16,
                                "roll": 0.79,
                                "yaw": 225.66,
                                "z": 721.9
                            },
                            {
                                "ImageName": "DSC00296.JPG",
                                "lat": -23.5983027,
                                "lon": -48.3320226,
                                "pitch": -7.35,
                                "roll": 0.54,
                                "yaw": 225.72,
                                "z": 722.03
                            },
                            {
                                "ImageName": "DSC00297.JPG",
                                "lat": -23.5984159,
                                "lon": -48.3321492,
                                "pitch": -7.81,
                                "roll": 0.96,
                                "yaw": 226.13,
                                "z": 722.12
                            },
                            {
                                "ImageName": "DSC00298.JPG",
                                "lat": -23.5985242,
                                "lon": -48.33227120000001,
                                "pitch": -7.6,
                                "roll": 0.49,
                                "yaw": 225.8,
                                "z": 722.33
                            },
                            {
                                "ImageName": "DSC00299.JPG",
                                "lat": -23.5986315,
                                "lon": -48.3323911,
                                "pitch": -7.04,
                                "roll": 1.29,
                                "yaw": 226.04,
                                "z": 722.57
                            },
                            {
                                "ImageName": "DSC00300.JPG",
                                "lat": -23.5987415,
                                "lon": -48.3325138,
                                "pitch": -6.84,
                                "roll": 1.49,
                                "yaw": 225.87,
                                "z": 722.96
                            },
                            {
                                "ImageName": "DSC00301.JPG",
                                "lat": -23.5988525,
                                "lon": -48.3326389,
                                "pitch": -6.4,
                                "roll": 1.35,
                                "yaw": 225.84,
                                "z": 723.63
                            },
                            {
                                "ImageName": "DSC00302.JPG",
                                "lat": -23.5989649,
                                "lon": -48.3327649,
                                "pitch": -6.79,
                                "roll": 1.26,
                                "yaw": 225.99,
                                "z": 724.36
                            },
                            {
                                "ImageName": "DSC00303.JPG",
                                "lat": -23.599071600000002,
                                "lon": -48.3328852,
                                "pitch": -6.0,
                                "roll": 1.11,
                                "yaw": 225.84,
                                "z": 725.21
                            },
                            {
                                "ImageName": "DSC00304.JPG",
                                "lat": -23.599180899999997,
                                "lon": -48.3330086,
                                "pitch": -6.64,
                                "roll": 0.38,
                                "yaw": 225.38,
                                "z": 726.19
                            },
                            {
                                "ImageName": "DSC00305.JPG",
                                "lat": -23.5992898,
                                "lon": -48.3331314,
                                "pitch": -3.29,
                                "roll": 0.39,
                                "yaw": 225.4,
                                "z": 727.33
                            },
                            {
                                "ImageName": "DSC00306.JPG",
                                "lat": -23.599397399999997,
                                "lon": -48.3332511,
                                "pitch": 1.11,
                                "roll": 0.88,
                                "yaw": 225.34,
                                "z": 728.5
                            },
                            {
                                "ImageName": "DSC00307.JPG",
                                "lat": -23.599501999999998,
                                "lon": -48.333368,
                                "pitch": 2.68,
                                "roll": -0.07,
                                "yaw": 225.01,
                                "z": 729.34
                            },
                            {
                                "ImageName": "DSC00308.JPG",
                                "lat": -23.5991987,
                                "lon": -48.3335138,
                                "pitch": 4.84,
                                "roll": 2.64,
                                "yaw": 6.07,
                                "z": 727.73
                            },
                            {
                                "ImageName": "DSC00309.JPG",
                                "lat": -23.5990853,
                                "lon": -48.333381599999996,
                                "pitch": -8.8,
                                "roll": 0.81,
                                "yaw": 44.51,
                                "z": 726.8
                            },
                            {
                                "ImageName": "DSC00310.JPG",
                                "lat": -23.5989736,
                                "lon": -48.3332589,
                                "pitch": -6.59,
                                "roll": 1.04,
                                "yaw": 44.92,
                                "z": 725.92
                            },
                            {
                                "ImageName": "DSC00311.JPG",
                                "lat": -23.5988568,
                                "lon": -48.333131,
                                "pitch": -6.08,
                                "roll": 0.79,
                                "yaw": 45.2,
                                "z": 724.88
                            },
                            {
                                "ImageName": "DSC00312.JPG",
                                "lat": -23.5987495,
                                "lon": -48.33301289999999,
                                "pitch": -5.85,
                                "roll": 1.28,
                                "yaw": 45.87,
                                "z": 723.96
                            },
                            {
                                "ImageName": "DSC00313.JPG",
                                "lat": -23.5986428,
                                "lon": -48.332893,
                                "pitch": -5.65,
                                "roll": 0.25,
                                "yaw": 45.23,
                                "z": 723.14
                            },
                            {
                                "ImageName": "DSC00314.JPG",
                                "lat": -23.5985303,
                                "lon": -48.3327674,
                                "pitch": -5.73,
                                "roll": 0.72,
                                "yaw": 45.6,
                                "z": 722.33
                            },
                            {
                                "ImageName": "DSC00315.JPG",
                                "lat": -23.598421300000002,
                                "lon": -48.3326447,
                                "pitch": -6.82,
                                "roll": 0.0,
                                "yaw": 45.71,
                                "z": 721.78
                            },
                            {
                                "ImageName": "DSC00316.JPG",
                                "lat": -23.5983128,
                                "lon": -48.332522499999996,
                                "pitch": -7.39,
                                "roll": -0.09,
                                "yaw": 45.77,
                                "z": 721.52
                            },
                            {
                                "ImageName": "DSC00317.JPG",
                                "lat": -23.598195899999997,
                                "lon": -48.332392299999995,
                                "pitch": -6.89,
                                "roll": 0.47,
                                "yaw": 45.85,
                                "z": 721.23
                            },
                            {
                                "ImageName": "DSC00318.JPG",
                                "lat": -23.5980931,
                                "lon": -48.332277500000004,
                                "pitch": -6.86,
                                "roll": 0.72,
                                "yaw": 46.12,
                                "z": 720.94
                            },
                            {
                                "ImageName": "DSC00319.JPG",
                                "lat": -23.5979841,
                                "lon": -48.332155,
                                "pitch": -6.21,
                                "roll": 0.65,
                                "yaw": 45.82,
                                "z": 720.83
                            },
                            {
                                "ImageName": "DSC00320.JPG",
                                "lat": -23.597873899999996,
                                "lon": -48.332031799999996,
                                "pitch": -6.77,
                                "roll": 0.9,
                                "yaw": 45.9,
                                "z": 720.69
                            },
                            {
                                "ImageName": "DSC00321.JPG",
                                "lat": -23.5977655,
                                "lon": -48.3319098,
                                "pitch": -6.99,
                                "roll": 0.85,
                                "yaw": 46.08,
                                "z": 720.59
                            },
                            {
                                "ImageName": "DSC00322.JPG",
                                "lat": -23.5976568,
                                "lon": -48.33178770000001,
                                "pitch": -7.46,
                                "roll": 0.87,
                                "yaw": 46.09,
                                "z": 720.47
                            },
                            {
                                "ImageName": "DSC00323.JPG",
                                "lat": -23.5975465,
                                "lon": -48.331663899999995,
                                "pitch": -5.61,
                                "roll": 0.84,
                                "yaw": 45.88,
                                "z": 720.31
                            },
                            {
                                "ImageName": "DSC00324.JPG",
                                "lat": -23.597438500000003,
                                "lon": -48.331543599999996,
                                "pitch": -2.17,
                                "roll": 1.24,
                                "yaw": 46.53,
                                "z": 720.48
                            },
                            {
                                "ImageName": "DSC00325.JPG",
                                "lat": -23.5973338,
                                "lon": -48.331426799999996,
                                "pitch": 2.41,
                                "roll": 1.43,
                                "yaw": 46.77,
                                "z": 720.82
                            },
                            {
                                "ImageName": "DSC00326.JPG",
                                "lat": -23.5972305,
                                "lon": -48.3313109,
                                "pitch": 3.72,
                                "roll": 2.71,
                                "yaw": 49.97,
                                "z": 721.34
                            },
                            {
                                "ImageName": "DSC00327.JPG",
                                "lat": -23.597010600000004,
                                "lon": -48.3315444,
                                "pitch": 5.3,
                                "roll": 0.37,
                                "yaw": 297.95,
                                "z": 721.4
                            },
                            {
                                "ImageName": "DSC00328.JPG",
                                "lat": -23.597132199999997,
                                "lon": -48.3316821,
                                "pitch": -9.37,
                                "roll": 0.45,
                                "yaw": 226.15,
                                "z": 721.05
                            },
                            {
                                "ImageName": "DSC00329.JPG",
                                "lat": -23.597240799999998,
                                "lon": -48.3318045,
                                "pitch": -7.31,
                                "roll": 0.92,
                                "yaw": 226.02,
                                "z": 720.78
                            },
                            {
                                "ImageName": "DSC00330.JPG",
                                "lat": -23.5973549,
                                "lon": -48.3319325,
                                "pitch": -7.06,
                                "roll": 1.1,
                                "yaw": 226.0,
                                "z": 720.38
                            },
                            {
                                "ImageName": "DSC00331.JPG",
                                "lat": -23.5974664,
                                "lon": -48.332058,
                                "pitch": -7.5,
                                "roll": 0.65,
                                "yaw": 225.67,
                                "z": 719.96
                            },
                            {
                                "ImageName": "DSC00332.JPG",
                                "lat": -23.5975759,
                                "lon": -48.332181299999995,
                                "pitch": -7.23,
                                "roll": 0.98,
                                "yaw": 225.9,
                                "z": 719.47
                            },
                            {
                                "ImageName": "DSC00333.JPG",
                                "lat": -23.5976908,
                                "lon": -48.332310799999995,
                                "pitch": -7.19,
                                "roll": 0.57,
                                "yaw": 225.43,
                                "z": 719.45
                            },
                            {
                                "ImageName": "DSC00334.JPG",
                                "lat": -23.5978021,
                                "lon": -48.3324352,
                                "pitch": -6.86,
                                "roll": 0.55,
                                "yaw": 225.42,
                                "z": 719.67
                            },
                            {
                                "ImageName": "DSC00335.JPG",
                                "lat": -23.597911899999996,
                                "lon": -48.3325578,
                                "pitch": -7.29,
                                "roll": 1.31,
                                "yaw": 226.0,
                                "z": 720.04
                            },
                            {
                                "ImageName": "DSC00336.JPG",
                                "lat": -23.598024,
                                "lon": -48.3326838,
                                "pitch": -7.49,
                                "roll": 1.14,
                                "yaw": 226.19,
                                "z": 720.34
                            },
                            {
                                "ImageName": "DSC00337.JPG",
                                "lat": -23.5981273,
                                "lon": -48.3328,
                                "pitch": -8.01,
                                "roll": 0.65,
                                "yaw": 225.68,
                                "z": 720.63
                            },
                            {
                                "ImageName": "DSC00338.JPG",
                                "lat": -23.598246399999997,
                                "lon": -48.3329331,
                                "pitch": -7.26,
                                "roll": 1.28,
                                "yaw": 226.23,
                                "z": 720.83
                            },
                            {
                                "ImageName": "DSC00339.JPG",
                                "lat": -23.5983529,
                                "lon": -48.333051700000006,
                                "pitch": -6.56,
                                "roll": 1.7,
                                "yaw": 226.34,
                                "z": 720.94
                            },
                            {
                                "ImageName": "DSC00340.JPG",
                                "lat": -23.5984609,
                                "lon": -48.333172600000005,
                                "pitch": -3.77,
                                "roll": 2.3,
                                "yaw": 226.78,
                                "z": 721.02
                            },
                            {
                                "ImageName": "DSC00341.JPG",
                                "lat": -23.598567000000003,
                                "lon": -48.333293100000006,
                                "pitch": -1.96,
                                "roll": 1.37,
                                "yaw": 226.26,
                                "z": 721.54
                            },
                            {
                                "ImageName": "DSC00342.JPG",
                                "lat": -23.5986753,
                                "lon": -48.3334148,
                                "pitch": 2.02,
                                "roll": 1.45,
                                "yaw": 226.08,
                                "z": 722.63
                            },
                            {
                                "ImageName": "DSC00343.JPG",
                                "lat": -23.5987802,
                                "lon": -48.333532700000006,
                                "pitch": 3.39,
                                "roll": 0.75,
                                "yaw": 225.1,
                                "z": 723.9
                            },
                            {
                                "ImageName": "DSC00344.JPG",
                                "lat": -23.5984678,
                                "lon": -48.333668599999996,
                                "pitch": 3.08,
                                "roll": 3.81,
                                "yaw": 6.52,
                                "z": 722.45
                            },
                            {
                                "ImageName": "DSC00345.JPG",
                                "lat": -23.598351899999997,
                                "lon": -48.333533,
                                "pitch": -8.78,
                                "roll": 0.4,
                                "yaw": 43.78,
                                "z": 721.63
                            },
                            {
                                "ImageName": "DSC00346.JPG",
                                "lat": -23.5982397,
                                "lon": -48.333409700000004,
                                "pitch": -6.43,
                                "roll": 0.96,
                                "yaw": 44.46,
                                "z": 721.2
                            },
                            {
                                "ImageName": "DSC00347.JPG",
                                "lat": -23.598125600000003,
                                "lon": -48.3332844,
                                "pitch": -6.3,
                                "roll": 0.54,
                                "yaw": 45.48,
                                "z": 720.75
                            },
                            {
                                "ImageName": "DSC00348.JPG",
                                "lat": -23.5980192,
                                "lon": -48.33316729999999,
                                "pitch": -6.94,
                                "roll": 0.73,
                                "yaw": 46.05,
                                "z": 720.56
                            },
                            {
                                "ImageName": "DSC00349.JPG",
                                "lat": -23.5979046,
                                "lon": -48.333038,
                                "pitch": -5.69,
                                "roll": 0.13,
                                "yaw": 45.44,
                                "z": 720.4
                            },
                            {
                                "ImageName": "DSC00350.JPG",
                                "lat": -23.597793600000003,
                                "lon": -48.3329147,
                                "pitch": -6.29,
                                "roll": 0.36,
                                "yaw": 45.75,
                                "z": 720.19
                            },
                            {
                                "ImageName": "DSC00351.JPG",
                                "lat": -23.5976878,
                                "lon": -48.3327961,
                                "pitch": -6.68,
                                "roll": 0.31,
                                "yaw": 45.97,
                                "z": 719.93
                            },
                            {
                                "ImageName": "DSC00352.JPG",
                                "lat": -23.597573399999998,
                                "lon": -48.3326673,
                                "pitch": -6.62,
                                "roll": 0.06,
                                "yaw": 45.67,
                                "z": 719.59
                            },
                            {
                                "ImageName": "DSC00353.JPG",
                                "lat": -23.597466,
                                "lon": -48.332546799999996,
                                "pitch": -6.86,
                                "roll": 0.07,
                                "yaw": 45.96,
                                "z": 719.41
                            },
                            {
                                "ImageName": "DSC00354.JPG",
                                "lat": -23.5973586,
                                "lon": -48.3324275,
                                "pitch": -6.87,
                                "roll": 0.63,
                                "yaw": 46.56,
                                "z": 719.53
                            },
                            {
                                "ImageName": "DSC00355.JPG",
                                "lat": -23.597250199999998,
                                "lon": -48.3323063,
                                "pitch": -6.54,
                                "roll": 0.57,
                                "yaw": 46.34,
                                "z": 719.76
                            },
                            {
                                "ImageName": "DSC00356.JPG",
                                "lat": -23.5971401,
                                "lon": -48.3321825,
                                "pitch": -4.35,
                                "roll": 0.89,
                                "yaw": 46.33,
                                "z": 720.2
                            },
                            {
                                "ImageName": "DSC00357.JPG",
                                "lat": -23.5970313,
                                "lon": -48.3320607,
                                "pitch": -1.55,
                                "roll": 0.75,
                                "yaw": 45.99,
                                "z": 720.68
                            },
                            {
                                "ImageName": "DSC00358.JPG",
                                "lat": -23.596929199999998,
                                "lon": -48.3319471,
                                "pitch": 2.81,
                                "roll": 1.12,
                                "yaw": 46.37,
                                "z": 721.03
                            },
                            {
                                "ImageName": "DSC00359.JPG",
                                "lat": -23.5968283,
                                "lon": -48.33183270000001,
                                "pitch": 4.34,
                                "roll": 1.37,
                                "yaw": 48.6,
                                "z": 721.56
                            },
                            {
                                "ImageName": "DSC00360.JPG",
                                "lat": -23.5966053,
                                "lon": -48.332065500000006,
                                "pitch": 4.65,
                                "roll": -0.26,
                                "yaw": 298.65,
                                "z": 721.87
                            },
                            {
                                "ImageName": "DSC00361.JPG",
                                "lat": -23.5967277,
                                "lon": -48.332201399999995,
                                "pitch": -8.73,
                                "roll": 1.19,
                                "yaw": 226.17,
                                "z": 721.75
                            },
                            {
                                "ImageName": "DSC00362.JPG",
                                "lat": -23.596837100000002,
                                "lon": -48.3323245,
                                "pitch": -6.44,
                                "roll": 1.44,
                                "yaw": 226.78,
                                "z": 721.42
                            },
                            {
                                "ImageName": "DSC00363.JPG",
                                "lat": -23.5969483,
                                "lon": -48.3324499,
                                "pitch": -6.47,
                                "roll": 1.63,
                                "yaw": 226.29,
                                "z": 720.92
                            },
                            {
                                "ImageName": "DSC00364.JPG",
                                "lat": -23.597056100000003,
                                "lon": -48.3325721,
                                "pitch": -5.64,
                                "roll": 1.39,
                                "yaw": 226.03,
                                "z": 720.5
                            },
                            {
                                "ImageName": "DSC00365.JPG",
                                "lat": -23.5971655,
                                "lon": -48.3326949,
                                "pitch": -6.04,
                                "roll": 1.37,
                                "yaw": 225.74,
                                "z": 720.12
                            },
                            {
                                "ImageName": "DSC00366.JPG",
                                "lat": -23.597277,
                                "lon": -48.332820500000004,
                                "pitch": -6.12,
                                "roll": 1.11,
                                "yaw": 225.46,
                                "z": 719.85
                            },
                            {
                                "ImageName": "DSC00367.JPG",
                                "lat": -23.5973853,
                                "lon": -48.332942200000005,
                                "pitch": -6.28,
                                "roll": 1.4,
                                "yaw": 225.71,
                                "z": 719.73
                            },
                            {
                                "ImageName": "DSC00368.JPG",
                                "lat": -23.597495600000002,
                                "lon": -48.333065999999995,
                                "pitch": -5.9,
                                "roll": 1.06,
                                "yaw": 225.7,
                                "z": 719.69
                            },
                            {
                                "ImageName": "DSC00369.JPG",
                                "lat": -23.597604500000003,
                                "lon": -48.3331878,
                                "pitch": -5.62,
                                "roll": 1.24,
                                "yaw": 225.6,
                                "z": 719.79
                            },
                            {
                                "ImageName": "DSC00370.JPG",
                                "lat": -23.5977111,
                                "lon": -48.333307,
                                "pitch": -5.28,
                                "roll": 1.62,
                                "yaw": 226.04,
                                "z": 720.03
                            },
                            {
                                "ImageName": "DSC00371.JPG",
                                "lat": -23.5978258,
                                "lon": -48.3334359,
                                "pitch": -2.31,
                                "roll": 1.26,
                                "yaw": 225.89,
                                "z": 720.38
                            },
                            {
                                "ImageName": "DSC00372.JPG",
                                "lat": -23.5979307,
                                "lon": -48.3335533,
                                "pitch": 1.32,
                                "roll": 1.52,
                                "yaw": 225.73,
                                "z": 720.87
                            }
                        ]
                    }
                },
                {
                    "size_type": "SMALL",
                    "name": "monjolao-22149",
                    "groveID": "-LowPdR61EefCtLH2KQa",
                    "index": "monjolao/22149",
                    "area": 5.485902355143335,
                    "commodity": "Oranges",
                    "grove_output": {
                        "name": "monjolao-22149",
                        "groveID": "-LowPdR61EefCtLH2KQa",
                        "number_of_files": "136",
                        "images_list": [
                            "DSC00049.JPG",
                            "DSC00050.JPG",
                            "DSC00051.JPG",
                            "DSC00052.JPG",
                            "DSC00053.JPG",
                            "DSC00054.JPG",
                            "DSC00055.JPG",
                            "DSC00056.JPG",
                            "DSC00057.JPG",
                            "DSC00058.JPG",
                            "DSC00059.JPG",
                            "DSC00060.JPG",
                            "DSC00061.JPG",
                            "DSC00062.JPG",
                            "DSC00063.JPG",
                            "DSC00064.JPG",
                            "DSC00065.JPG",
                            "DSC00066.JPG",
                            "DSC00067.JPG",
                            "DSC00068.JPG",
                            "DSC00069.JPG",
                            "DSC00070.JPG",
                            "DSC00071.JPG",
                            "DSC00072.JPG",
                            "DSC00073.JPG",
                            "DSC00074.JPG",
                            "DSC00075.JPG",
                            "DSC00076.JPG",
                            "DSC00077.JPG",
                            "DSC00078.JPG",
                            "DSC00079.JPG",
                            "DSC00080.JPG",
                            "DSC00081.JPG",
                            "DSC00082.JPG",
                            "DSC00083.JPG",
                            "DSC00084.JPG",
                            "DSC00085.JPG",
                            "DSC00086.JPG",
                            "DSC00087.JPG",
                            "DSC00088.JPG",
                            "DSC00089.JPG",
                            "DSC00090.JPG",
                            "DSC00091.JPG",
                            "DSC00092.JPG",
                            "DSC00093.JPG",
                            "DSC00094.JPG",
                            "DSC00095.JPG",
                            "DSC00096.JPG",
                            "DSC00097.JPG",
                            "DSC00098.JPG",
                            "DSC00099.JPG",
                            "DSC00100.JPG",
                            "DSC00101.JPG",
                            "DSC00102.JPG",
                            "DSC00103.JPG",
                            "DSC00104.JPG",
                            "DSC00105.JPG",
                            "DSC00106.JPG",
                            "DSC00107.JPG",
                            "DSC00108.JPG",
                            "DSC00109.JPG",
                            "DSC00110.JPG",
                            "DSC00111.JPG",
                            "DSC00112.JPG",
                            "DSC00113.JPG",
                            "DSC00114.JPG",
                            "DSC00115.JPG",
                            "DSC00116.JPG",
                            "DSC00117.JPG",
                            "DSC00118.JPG",
                            "DSC00119.JPG",
                            "DSC00120.JPG",
                            "DSC00121.JPG",
                            "DSC00122.JPG",
                            "DSC00123.JPG",
                            "DSC00124.JPG",
                            "DSC00125.JPG",
                            "DSC00126.JPG",
                            "DSC00127.JPG",
                            "DSC00128.JPG",
                            "DSC00129.JPG",
                            "DSC00130.JPG",
                            "DSC00131.JPG",
                            "DSC00132.JPG",
                            "DSC00133.JPG",
                            "DSC00134.JPG",
                            "DSC00135.JPG",
                            "DSC00136.JPG",
                            "DSC00137.JPG",
                            "DSC00138.JPG",
                            "DSC00139.JPG",
                            "DSC00140.JPG",
                            "DSC00141.JPG",
                            "DSC00142.JPG",
                            "DSC00143.JPG",
                            "DSC00144.JPG",
                            "DSC00145.JPG",
                            "DSC00146.JPG",
                            "DSC00147.JPG",
                            "DSC00148.JPG",
                            "DSC00149.JPG",
                            "DSC00150.JPG",
                            "DSC00151.JPG",
                            "DSC00152.JPG",
                            "DSC00153.JPG",
                            "DSC00154.JPG",
                            "DSC00155.JPG",
                            "DSC00156.JPG",
                            "DSC00157.JPG",
                            "DSC00158.JPG",
                            "DSC00159.JPG",
                            "DSC00160.JPG",
                            "DSC00161.JPG",
                            "DSC00162.JPG",
                            "DSC00163.JPG",
                            "DSC00164.JPG",
                            "DSC00165.JPG",
                            "DSC00166.JPG",
                            "DSC00167.JPG",
                            "DSC00168.JPG",
                            "DSC00169.JPG",
                            "DSC00170.JPG",
                            "DSC00171.JPG",
                            "DSC00172.JPG",
                            "DSC00173.JPG",
                            "DSC00174.JPG",
                            "DSC00175.JPG",
                            "DSC00176.JPG",
                            "DSC00177.JPG",
                            "DSC00178.JPG",
                            "DSC00179.JPG",
                            "DSC00180.JPG",
                            "DSC00181.JPG",
                            "DSC00182.JPG",
                            "DSC00183.JPG",
                            "DSC00184.JPG"
                        ],
                        "splitter_location": [
                            {
                                "ImageName": "DSC00049.JPG",
                                "lat": -23.598817999999998,
                                "lon": -48.322008700000005,
                                "pitch": -8.32,
                                "roll": 0.17,
                                "yaw": 201.52,
                                "z": 722.7
                            },
                            {
                                "ImageName": "DSC00050.JPG",
                                "lat": -23.598971600000002,
                                "lon": -48.3220722,
                                "pitch": -6.73,
                                "roll": 0.76,
                                "yaw": 202.24,
                                "z": 723.42
                            },
                            {
                                "ImageName": "DSC00051.JPG",
                                "lat": -23.599115,
                                "lon": -48.3221341,
                                "pitch": -6.66,
                                "roll": 0.85,
                                "yaw": 202.34,
                                "z": 724.12
                            },
                            {
                                "ImageName": "DSC00052.JPG",
                                "lat": -23.599259399999998,
                                "lon": -48.3221978,
                                "pitch": -7.23,
                                "roll": 0.39,
                                "yaw": 202.15,
                                "z": 724.99
                            },
                            {
                                "ImageName": "DSC00053.JPG",
                                "lat": -23.599401699999998,
                                "lon": -48.3222614,
                                "pitch": -7.75,
                                "roll": -0.09,
                                "yaw": 201.71,
                                "z": 725.81
                            },
                            {
                                "ImageName": "DSC00054.JPG",
                                "lat": -23.5995514,
                                "lon": -48.3223269,
                                "pitch": -7.27,
                                "roll": 0.28,
                                "yaw": 201.64,
                                "z": 725.86
                            },
                            {
                                "ImageName": "DSC00055.JPG",
                                "lat": -23.599696100000003,
                                "lon": -48.322390000000006,
                                "pitch": -7.14,
                                "roll": 0.3,
                                "yaw": 201.45,
                                "z": 725.69
                            },
                            {
                                "ImageName": "DSC00056.JPG",
                                "lat": -23.5998415,
                                "lon": -48.3224532,
                                "pitch": -7.33,
                                "roll": 0.44,
                                "yaw": 201.62,
                                "z": 725.41
                            },
                            {
                                "ImageName": "DSC00057.JPG",
                                "lat": -23.5999922,
                                "lon": -48.3225183,
                                "pitch": -7.44,
                                "roll": 0.93,
                                "yaw": 201.69,
                                "z": 725.15
                            },
                            {
                                "ImageName": "DSC00058.JPG",
                                "lat": -23.6001302,
                                "lon": -48.3225781,
                                "pitch": -7.1,
                                "roll": 0.86,
                                "yaw": 201.98,
                                "z": 724.79
                            },
                            {
                                "ImageName": "DSC00059.JPG",
                                "lat": -23.600278,
                                "lon": -48.3226424,
                                "pitch": -3.72,
                                "roll": 0.93,
                                "yaw": 202.1,
                                "z": 724.52
                            },
                            {
                                "ImageName": "DSC00060.JPG",
                                "lat": -23.6004247,
                                "lon": -48.3227057,
                                "pitch": 0.0,
                                "roll": 1.4,
                                "yaw": 202.14,
                                "z": 724.24
                            },
                            {
                                "ImageName": "DSC00061.JPG",
                                "lat": -23.600565600000003,
                                "lon": -48.3227658,
                                "pitch": 2.37,
                                "roll": 1.97,
                                "yaw": 203.03,
                                "z": 724.01
                            },
                            {
                                "ImageName": "DSC00062.JPG",
                                "lat": -23.6006935,
                                "lon": -48.3228235,
                                "pitch": 5.89,
                                "roll": 1.71,
                                "yaw": 206.41,
                                "z": 724.13
                            },
                            {
                                "ImageName": "DSC00063.JPG",
                                "lat": -23.6007211,
                                "lon": -48.3231979,
                                "pitch": 5.61,
                                "roll": 3.83,
                                "yaw": 288.87,
                                "z": 726.36
                            },
                            {
                                "ImageName": "DSC00064.JPG",
                                "lat": -23.600562399999998,
                                "lon": -48.3231282,
                                "pitch": -8.75,
                                "roll": 0.29,
                                "yaw": 20.29,
                                "z": 725.97
                            },
                            {
                                "ImageName": "DSC00065.JPG",
                                "lat": -23.6004134,
                                "lon": -48.323065,
                                "pitch": -7.51,
                                "roll": 0.13,
                                "yaw": 20.68,
                                "z": 725.79
                            },
                            {
                                "ImageName": "DSC00066.JPG",
                                "lat": -23.6002573,
                                "lon": -48.3229993,
                                "pitch": -7.57,
                                "roll": -0.14,
                                "yaw": 21.58,
                                "z": 725.61
                            },
                            {
                                "ImageName": "DSC00067.JPG",
                                "lat": -23.600115,
                                "lon": -48.3229389,
                                "pitch": -7.31,
                                "roll": 1.01,
                                "yaw": 21.82,
                                "z": 725.53
                            },
                            {
                                "ImageName": "DSC00068.JPG",
                                "lat": -23.5999685,
                                "lon": -48.3228753,
                                "pitch": -7.52,
                                "roll": 0.65,
                                "yaw": 21.92,
                                "z": 725.51
                            },
                            {
                                "ImageName": "DSC00069.JPG",
                                "lat": -23.5998206,
                                "lon": -48.322810499999996,
                                "pitch": -7.94,
                                "roll": 0.7,
                                "yaw": 22.04,
                                "z": 725.57
                            },
                            {
                                "ImageName": "DSC00070.JPG",
                                "lat": -23.5996757,
                                "lon": -48.3227469,
                                "pitch": -7.39,
                                "roll": 0.15,
                                "yaw": 21.72,
                                "z": 725.79
                            },
                            {
                                "ImageName": "DSC00071.JPG",
                                "lat": -23.599529999999998,
                                "lon": -48.322683700000006,
                                "pitch": -7.58,
                                "roll": 0.98,
                                "yaw": 21.8,
                                "z": 726.03
                            },
                            {
                                "ImageName": "DSC00072.JPG",
                                "lat": -23.599383399999997,
                                "lon": -48.3226203,
                                "pitch": -7.0,
                                "roll": 0.76,
                                "yaw": 22.03,
                                "z": 726.38
                            },
                            {
                                "ImageName": "DSC00073.JPG",
                                "lat": -23.5992402,
                                "lon": -48.3225582,
                                "pitch": -6.6,
                                "roll": 1.08,
                                "yaw": 21.95,
                                "z": 726.5
                            },
                            {
                                "ImageName": "DSC00074.JPG",
                                "lat": -23.5990958,
                                "lon": -48.3224953,
                                "pitch": -6.32,
                                "roll": 0.87,
                                "yaw": 21.65,
                                "z": 725.9
                            },
                            {
                                "ImageName": "DSC00075.JPG",
                                "lat": -23.5989537,
                                "lon": -48.322433399999994,
                                "pitch": -5.12,
                                "roll": 1.11,
                                "yaw": 22.08,
                                "z": 725.15
                            },
                            {
                                "ImageName": "DSC00076.JPG",
                                "lat": -23.5988108,
                                "lon": -48.322371000000004,
                                "pitch": -2.37,
                                "roll": 0.92,
                                "yaw": 21.8,
                                "z": 724.18
                            },
                            {
                                "ImageName": "DSC00077.JPG",
                                "lat": -23.5986671,
                                "lon": -48.3223093,
                                "pitch": 1.73,
                                "roll": 1.24,
                                "yaw": 21.73,
                                "z": 723.22
                            },
                            {
                                "ImageName": "DSC00078.JPG",
                                "lat": -23.598532000000002,
                                "lon": -48.3222519,
                                "pitch": 2.48,
                                "roll": 1.98,
                                "yaw": 23.15,
                                "z": 722.41
                            },
                            {
                                "ImageName": "DSC00079.JPG",
                                "lat": -23.598285100000002,
                                "lon": -48.3225041,
                                "pitch": 5.4,
                                "roll": 1.24,
                                "yaw": 287.64,
                                "z": 721.88
                            },
                            {
                                "ImageName": "DSC00080.JPG",
                                "lat": -23.598442499999997,
                                "lon": -48.3225732,
                                "pitch": -8.4,
                                "roll": 0.5,
                                "yaw": 201.97,
                                "z": 721.77
                            },
                            {
                                "ImageName": "DSC00081.JPG",
                                "lat": -23.5985933,
                                "lon": -48.3226394,
                                "pitch": -6.89,
                                "roll": 0.78,
                                "yaw": 201.52,
                                "z": 722.42
                            },
                            {
                                "ImageName": "DSC00082.JPG",
                                "lat": -23.598741,
                                "lon": -48.322704200000004,
                                "pitch": -6.71,
                                "roll": 0.46,
                                "yaw": 201.3,
                                "z": 723.17
                            },
                            {
                                "ImageName": "DSC00083.JPG",
                                "lat": -23.5988853,
                                "lon": -48.322767299999995,
                                "pitch": -6.93,
                                "roll": 0.54,
                                "yaw": 201.3,
                                "z": 723.83
                            },
                            {
                                "ImageName": "DSC00084.JPG",
                                "lat": -23.5990323,
                                "lon": -48.3228313,
                                "pitch": -7.37,
                                "roll": 0.73,
                                "yaw": 201.66,
                                "z": 724.43
                            },
                            {
                                "ImageName": "DSC00085.JPG",
                                "lat": -23.5991805,
                                "lon": -48.322895700000004,
                                "pitch": -7.59,
                                "roll": 0.79,
                                "yaw": 201.7,
                                "z": 725.15
                            },
                            {
                                "ImageName": "DSC00086.JPG",
                                "lat": -23.5993236,
                                "lon": -48.3229574,
                                "pitch": -7.86,
                                "roll": 0.83,
                                "yaw": 201.82,
                                "z": 725.7
                            },
                            {
                                "ImageName": "DSC00087.JPG",
                                "lat": -23.599471899999998,
                                "lon": -48.3230221,
                                "pitch": -7.84,
                                "roll": 0.81,
                                "yaw": 201.64,
                                "z": 725.93
                            },
                            {
                                "ImageName": "DSC00088.JPG",
                                "lat": -23.5996152,
                                "lon": -48.3230844,
                                "pitch": -7.92,
                                "roll": 0.89,
                                "yaw": 201.67,
                                "z": 725.87
                            },
                            {
                                "ImageName": "DSC00089.JPG",
                                "lat": -23.5997569,
                                "lon": -48.323146200000004,
                                "pitch": -7.33,
                                "roll": 0.63,
                                "yaw": 201.99,
                                "z": 725.81
                            },
                            {
                                "ImageName": "DSC00090.JPG",
                                "lat": -23.599903100000002,
                                "lon": -48.3232097,
                                "pitch": -7.42,
                                "roll": 0.56,
                                "yaw": 201.66,
                                "z": 725.84
                            },
                            {
                                "ImageName": "DSC00091.JPG",
                                "lat": -23.6000491,
                                "lon": -48.3232726,
                                "pitch": -6.98,
                                "roll": 0.95,
                                "yaw": 201.89,
                                "z": 725.99
                            },
                            {
                                "ImageName": "DSC00092.JPG",
                                "lat": -23.6001953,
                                "lon": -48.3233356,
                                "pitch": -6.81,
                                "roll": 1.28,
                                "yaw": 201.72,
                                "z": 726.29
                            },
                            {
                                "ImageName": "DSC00093.JPG",
                                "lat": -23.6003378,
                                "lon": -48.3233975,
                                "pitch": -4.15,
                                "roll": 1.22,
                                "yaw": 202.03,
                                "z": 726.64
                            },
                            {
                                "ImageName": "DSC00094.JPG",
                                "lat": -23.6004866,
                                "lon": -48.323462400000004,
                                "pitch": 0.47,
                                "roll": 1.52,
                                "yaw": 202.56,
                                "z": 727.17
                            },
                            {
                                "ImageName": "DSC00095.JPG",
                                "lat": -23.600626199999997,
                                "lon": -48.3235229,
                                "pitch": 2.74,
                                "roll": 1.15,
                                "yaw": 201.99,
                                "z": 727.87
                            },
                            {
                                "ImageName": "DSC00096.JPG",
                                "lat": -23.6008801,
                                "lon": -48.3239959,
                                "pitch": 5.65,
                                "roll": 2.53,
                                "yaw": 263.97,
                                "z": 732.88
                            },
                            {
                                "ImageName": "DSC00097.JPG",
                                "lat": -23.600718899999997,
                                "lon": -48.3239269,
                                "pitch": -8.47,
                                "roll": 0.6,
                                "yaw": 20.45,
                                "z": 731.86
                            },
                            {
                                "ImageName": "DSC00098.JPG",
                                "lat": -23.6005715,
                                "lon": -48.323865399999995,
                                "pitch": -7.23,
                                "roll": 0.81,
                                "yaw": 21.39,
                                "z": 730.88
                            },
                            {
                                "ImageName": "DSC00099.JPG",
                                "lat": -23.6004214,
                                "lon": -48.3238015,
                                "pitch": -7.51,
                                "roll": 1.0,
                                "yaw": 21.73,
                                "z": 729.81
                            },
                            {
                                "ImageName": "DSC00100.JPG",
                                "lat": -23.600279999999998,
                                "lon": -48.3237403,
                                "pitch": -7.3,
                                "roll": 0.92,
                                "yaw": 22.29,
                                "z": 728.91
                            },
                            {
                                "ImageName": "DSC00101.JPG",
                                "lat": -23.6001294,
                                "lon": -48.3236744,
                                "pitch": -7.08,
                                "roll": 0.68,
                                "yaw": 21.65,
                                "z": 728.06
                            },
                            {
                                "ImageName": "DSC00102.JPG",
                                "lat": -23.5999802,
                                "lon": -48.3236084,
                                "pitch": -7.3,
                                "roll": 0.37,
                                "yaw": 21.59,
                                "z": 727.3
                            },
                            {
                                "ImageName": "DSC00103.JPG",
                                "lat": -23.5998397,
                                "lon": -48.3235471,
                                "pitch": -6.82,
                                "roll": 0.67,
                                "yaw": 21.74,
                                "z": 726.63
                            },
                            {
                                "ImageName": "DSC00104.JPG",
                                "lat": -23.5996902,
                                "lon": -48.3234822,
                                "pitch": -7.5,
                                "roll": 0.74,
                                "yaw": 21.69,
                                "z": 726.07
                            },
                            {
                                "ImageName": "DSC00105.JPG",
                                "lat": -23.5995457,
                                "lon": -48.3234197,
                                "pitch": -6.95,
                                "roll": 1.2,
                                "yaw": 21.72,
                                "z": 725.68
                            },
                            {
                                "ImageName": "DSC00106.JPG",
                                "lat": -23.5994008,
                                "lon": -48.32335689999999,
                                "pitch": -6.86,
                                "roll": 1.49,
                                "yaw": 22.26,
                                "z": 725.41
                            },
                            {
                                "ImageName": "DSC00107.JPG",
                                "lat": -23.599256399999998,
                                "lon": -48.323293799999995,
                                "pitch": -7.34,
                                "roll": 0.75,
                                "yaw": 21.54,
                                "z": 725.15
                            },
                            {
                                "ImageName": "DSC00108.JPG",
                                "lat": -23.5991138,
                                "lon": -48.323231799999995,
                                "pitch": -6.83,
                                "roll": 1.35,
                                "yaw": 22.03,
                                "z": 724.75
                            },
                            {
                                "ImageName": "DSC00109.JPG",
                                "lat": -23.598966600000004,
                                "lon": -48.3231679,
                                "pitch": -7.27,
                                "roll": 1.38,
                                "yaw": 22.07,
                                "z": 724.3
                            },
                            {
                                "ImageName": "DSC00110.JPG",
                                "lat": -23.5988223,
                                "lon": -48.323105,
                                "pitch": -5.05,
                                "roll": 1.21,
                                "yaw": 21.82,
                                "z": 723.77
                            },
                            {
                                "ImageName": "DSC00111.JPG",
                                "lat": -23.598672699999998,
                                "lon": -48.3230402,
                                "pitch": -0.89,
                                "roll": 1.23,
                                "yaw": 22.01,
                                "z": 723.19
                            },
                            {
                                "ImageName": "DSC00112.JPG",
                                "lat": -23.598536499999998,
                                "lon": -48.32298170000001,
                                "pitch": 2.82,
                                "roll": 1.09,
                                "yaw": 21.35,
                                "z": 722.53
                            },
                            {
                                "ImageName": "DSC00113.JPG",
                                "lat": -23.598398,
                                "lon": -48.3229219,
                                "pitch": 3.85,
                                "roll": 1.55,
                                "yaw": 24.16,
                                "z": 722.07
                            },
                            {
                                "ImageName": "DSC00114.JPG",
                                "lat": -23.5984562,
                                "lon": -48.32330770000001,
                                "pitch": 2.98,
                                "roll": -0.53,
                                "yaw": 247.7,
                                "z": 722.08
                            },
                            {
                                "ImageName": "DSC00115.JPG",
                                "lat": -23.5986161,
                                "lon": -48.323378600000005,
                                "pitch": -9.34,
                                "roll": 0.85,
                                "yaw": 201.84,
                                "z": 722.37
                            },
                            {
                                "ImageName": "DSC00116.JPG",
                                "lat": -23.598764000000003,
                                "lon": -48.323442799999995,
                                "pitch": -7.03,
                                "roll": 1.26,
                                "yaw": 201.61,
                                "z": 722.83
                            },
                            {
                                "ImageName": "DSC00117.JPG",
                                "lat": -23.5989045,
                                "lon": -48.3235041,
                                "pitch": -6.81,
                                "roll": 1.06,
                                "yaw": 201.84,
                                "z": 723.28
                            },
                            {
                                "ImageName": "DSC00118.JPG",
                                "lat": -23.5990525,
                                "lon": -48.3235691,
                                "pitch": -6.52,
                                "roll": 0.95,
                                "yaw": 201.33,
                                "z": 723.79
                            },
                            {
                                "ImageName": "DSC00119.JPG",
                                "lat": -23.5991979,
                                "lon": -48.3236323,
                                "pitch": -6.87,
                                "roll": 0.9,
                                "yaw": 201.45,
                                "z": 724.37
                            },
                            {
                                "ImageName": "DSC00120.JPG",
                                "lat": -23.5993445,
                                "lon": -48.32369620000001,
                                "pitch": -6.87,
                                "roll": 0.66,
                                "yaw": 201.41,
                                "z": 724.95
                            },
                            {
                                "ImageName": "DSC00121.JPG",
                                "lat": -23.599482899999998,
                                "lon": -48.3237565,
                                "pitch": -6.74,
                                "roll": 0.3,
                                "yaw": 201.7,
                                "z": 725.48
                            },
                            {
                                "ImageName": "DSC00122.JPG",
                                "lat": -23.5996365,
                                "lon": -48.3238225,
                                "pitch": -7.21,
                                "roll": 1.02,
                                "yaw": 201.71,
                                "z": 726.12
                            },
                            {
                                "ImageName": "DSC00123.JPG",
                                "lat": -23.5997861,
                                "lon": -48.323887400000004,
                                "pitch": -6.5,
                                "roll": 0.66,
                                "yaw": 201.68,
                                "z": 726.83
                            },
                            {
                                "ImageName": "DSC00124.JPG",
                                "lat": -23.5999228,
                                "lon": -48.323947,
                                "pitch": -6.47,
                                "roll": 0.72,
                                "yaw": 201.71,
                                "z": 727.55
                            },
                            {
                                "ImageName": "DSC00125.JPG",
                                "lat": -23.600068399999998,
                                "lon": -48.3240097,
                                "pitch": -6.75,
                                "roll": 1.33,
                                "yaw": 201.98,
                                "z": 728.4
                            },
                            {
                                "ImageName": "DSC00126.JPG",
                                "lat": -23.6002148,
                                "lon": -48.3240735,
                                "pitch": -6.59,
                                "roll": 0.89,
                                "yaw": 201.77,
                                "z": 729.24
                            },
                            {
                                "ImageName": "DSC00127.JPG",
                                "lat": -23.6003586,
                                "lon": -48.324136700000004,
                                "pitch": -7.03,
                                "roll": 0.79,
                                "yaw": 201.8,
                                "z": 730.4
                            },
                            {
                                "ImageName": "DSC00128.JPG",
                                "lat": -23.600503500000002,
                                "lon": -48.3241995,
                                "pitch": -6.68,
                                "roll": 1.09,
                                "yaw": 201.59,
                                "z": 731.66
                            },
                            {
                                "ImageName": "DSC00129.JPG",
                                "lat": -23.6006464,
                                "lon": -48.3242615,
                                "pitch": -3.89,
                                "roll": 0.93,
                                "yaw": 201.75,
                                "z": 732.97
                            },
                            {
                                "ImageName": "DSC00130.JPG",
                                "lat": -23.600792499999997,
                                "lon": -48.3243248,
                                "pitch": 0.35,
                                "roll": 0.76,
                                "yaw": 201.92,
                                "z": 734.51
                            },
                            {
                                "ImageName": "DSC00131.JPG",
                                "lat": -23.6009294,
                                "lon": -48.3243838,
                                "pitch": 2.89,
                                "roll": 1.48,
                                "yaw": 202.32,
                                "z": 736.07
                            },
                            {
                                "ImageName": "DSC00132.JPG",
                                "lat": -23.601069600000002,
                                "lon": -48.324808399999995,
                                "pitch": 6.01,
                                "roll": 2.02,
                                "yaw": 282.96,
                                "z": 736.17
                            },
                            {
                                "ImageName": "DSC00133.JPG",
                                "lat": -23.600912,
                                "lon": -48.324738599999996,
                                "pitch": -8.22,
                                "roll": 0.52,
                                "yaw": 19.97,
                                "z": 735.47
                            },
                            {
                                "ImageName": "DSC00134.JPG",
                                "lat": -23.6007659,
                                "lon": -48.3246779,
                                "pitch": -6.98,
                                "roll": 0.95,
                                "yaw": 21.05,
                                "z": 734.95
                            },
                            {
                                "ImageName": "DSC00135.JPG",
                                "lat": -23.600614800000002,
                                "lon": -48.3246134,
                                "pitch": -7.05,
                                "roll": 0.92,
                                "yaw": 21.4,
                                "z": 734.35
                            },
                            {
                                "ImageName": "DSC00136.JPG",
                                "lat": -23.6004668,
                                "lon": -48.3245492,
                                "pitch": -7.42,
                                "roll": 0.51,
                                "yaw": 21.13,
                                "z": 733.66
                            },
                            {
                                "ImageName": "DSC00137.JPG",
                                "lat": -23.600322199999997,
                                "lon": -48.3244867,
                                "pitch": -7.32,
                                "roll": 1.01,
                                "yaw": 21.49,
                                "z": 732.85
                            },
                            {
                                "ImageName": "DSC00138.JPG",
                                "lat": -23.6001758,
                                "lon": -48.324422399999996,
                                "pitch": -8.0,
                                "roll": 0.56,
                                "yaw": 21.32,
                                "z": 732.0
                            },
                            {
                                "ImageName": "DSC00139.JPG",
                                "lat": -23.600028,
                                "lon": -48.3243578,
                                "pitch": -8.02,
                                "roll": 0.4,
                                "yaw": 21.38,
                                "z": 730.8
                            },
                            {
                                "ImageName": "DSC00140.JPG",
                                "lat": -23.5998871,
                                "lon": -48.3242967,
                                "pitch": -8.36,
                                "roll": 0.27,
                                "yaw": 21.42,
                                "z": 729.67
                            },
                            {
                                "ImageName": "DSC00141.JPG",
                                "lat": -23.5997344,
                                "lon": -48.324230799999995,
                                "pitch": -7.69,
                                "roll": 1.37,
                                "yaw": 22.1,
                                "z": 728.48
                            },
                            {
                                "ImageName": "DSC00142.JPG",
                                "lat": -23.5995939,
                                "lon": -48.3241696,
                                "pitch": -7.03,
                                "roll": 0.76,
                                "yaw": 22.0,
                                "z": 727.51
                            },
                            {
                                "ImageName": "DSC00143.JPG",
                                "lat": -23.5994495,
                                "lon": -48.3241063,
                                "pitch": -8.19,
                                "roll": 0.79,
                                "yaw": 21.25,
                                "z": 726.59
                            },
                            {
                                "ImageName": "DSC00144.JPG",
                                "lat": -23.5993062,
                                "lon": -48.3240438,
                                "pitch": -8.02,
                                "roll": 0.71,
                                "yaw": 21.45,
                                "z": 725.81
                            },
                            {
                                "ImageName": "DSC00145.JPG",
                                "lat": -23.5991603,
                                "lon": -48.3239807,
                                "pitch": -7.4,
                                "roll": 1.14,
                                "yaw": 21.82,
                                "z": 725.21
                            },
                            {
                                "ImageName": "DSC00146.JPG",
                                "lat": -23.5990138,
                                "lon": -48.323917,
                                "pitch": -5.79,
                                "roll": 0.71,
                                "yaw": 21.66,
                                "z": 724.69
                            },
                            {
                                "ImageName": "DSC00147.JPG",
                                "lat": -23.5988682,
                                "lon": -48.323854,
                                "pitch": -2.36,
                                "roll": 0.92,
                                "yaw": 21.67,
                                "z": 724.18
                            },
                            {
                                "ImageName": "DSC00148.JPG",
                                "lat": -23.5987285,
                                "lon": -48.3237941,
                                "pitch": 1.6,
                                "roll": 1.06,
                                "yaw": 22.03,
                                "z": 723.61
                            },
                            {
                                "ImageName": "DSC00149.JPG",
                                "lat": -23.598589699999998,
                                "lon": -48.3237344,
                                "pitch": 2.92,
                                "roll": 1.67,
                                "yaw": 23.42,
                                "z": 723.01
                            },
                            {
                                "ImageName": "DSC00150.JPG",
                                "lat": -23.5986296,
                                "lon": -48.3241126,
                                "pitch": 2.14,
                                "roll": -1.2,
                                "yaw": 249.56,
                                "z": 723.75
                            },
                            {
                                "ImageName": "DSC00151.JPG",
                                "lat": -23.5987873,
                                "lon": -48.324181700000004,
                                "pitch": -8.4,
                                "roll": 1.5,
                                "yaw": 201.55,
                                "z": 724.08
                            },
                            {
                                "ImageName": "DSC00152.JPG",
                                "lat": -23.598934,
                                "lon": -48.3242465,
                                "pitch": -6.93,
                                "roll": 0.9,
                                "yaw": 201.3,
                                "z": 724.47
                            },
                            {
                                "ImageName": "DSC00153.JPG",
                                "lat": -23.599084299999998,
                                "lon": -48.3243117,
                                "pitch": -6.38,
                                "roll": 0.84,
                                "yaw": 201.39,
                                "z": 724.99
                            },
                            {
                                "ImageName": "DSC00154.JPG",
                                "lat": -23.5992283,
                                "lon": -48.3243739,
                                "pitch": -6.5,
                                "roll": 0.83,
                                "yaw": 201.59,
                                "z": 725.41
                            },
                            {
                                "ImageName": "DSC00155.JPG",
                                "lat": -23.5993743,
                                "lon": -48.3244373,
                                "pitch": -6.7,
                                "roll": 0.87,
                                "yaw": 201.68,
                                "z": 725.8
                            },
                            {
                                "ImageName": "DSC00156.JPG",
                                "lat": -23.5995197,
                                "lon": -48.3245004,
                                "pitch": -7.2,
                                "roll": 1.12,
                                "yaw": 201.56,
                                "z": 726.58
                            },
                            {
                                "ImageName": "DSC00157.JPG",
                                "lat": -23.5996654,
                                "lon": -48.3245636,
                                "pitch": -6.81,
                                "roll": 1.03,
                                "yaw": 201.64,
                                "z": 727.35
                            },
                            {
                                "ImageName": "DSC00158.JPG",
                                "lat": -23.5998087,
                                "lon": -48.3246263,
                                "pitch": -6.64,
                                "roll": 0.87,
                                "yaw": 201.61,
                                "z": 728.19
                            },
                            {
                                "ImageName": "DSC00159.JPG",
                                "lat": -23.5999628,
                                "lon": -48.32469329999999,
                                "pitch": -6.72,
                                "roll": 1.05,
                                "yaw": 201.74,
                                "z": 728.99
                            },
                            {
                                "ImageName": "DSC00160.JPG",
                                "lat": -23.6001004,
                                "lon": -48.324753,
                                "pitch": -7.25,
                                "roll": 1.37,
                                "yaw": 201.75,
                                "z": 729.56
                            },
                            {
                                "ImageName": "DSC00161.JPG",
                                "lat": -23.6002452,
                                "lon": -48.3248159,
                                "pitch": -6.97,
                                "roll": 1.39,
                                "yaw": 201.77,
                                "z": 730.44
                            },
                            {
                                "ImageName": "DSC00162.JPG",
                                "lat": -23.6003906,
                                "lon": -48.324878999999996,
                                "pitch": -6.94,
                                "roll": 1.38,
                                "yaw": 201.82,
                                "z": 731.21
                            },
                            {
                                "ImageName": "DSC00163.JPG",
                                "lat": -23.600536399999996,
                                "lon": -48.324942799999995,
                                "pitch": -7.0,
                                "roll": 1.05,
                                "yaw": 201.64,
                                "z": 731.78
                            },
                            {
                                "ImageName": "DSC00164.JPG",
                                "lat": -23.6006802,
                                "lon": -48.325005299999994,
                                "pitch": -3.89,
                                "roll": 1.22,
                                "yaw": 201.75,
                                "z": 732.26
                            },
                            {
                                "ImageName": "DSC00165.JPG",
                                "lat": -23.600824499999998,
                                "lon": -48.325068,
                                "pitch": -0.16,
                                "roll": 1.14,
                                "yaw": 201.9,
                                "z": 732.68
                            },
                            {
                                "ImageName": "DSC00166.JPG",
                                "lat": -23.6009628,
                                "lon": -48.325128,
                                "pitch": 2.75,
                                "roll": 0.95,
                                "yaw": 201.75,
                                "z": 733.08
                            },
                            {
                                "ImageName": "DSC00167.JPG",
                                "lat": -23.6010922,
                                "lon": -48.3251846,
                                "pitch": 6.81,
                                "roll": 1.1,
                                "yaw": 203.33,
                                "z": 733.56
                            },
                            {
                                "ImageName": "DSC00168.JPG",
                                "lat": -23.601129500000003,
                                "lon": -48.3255635,
                                "pitch": 4.88,
                                "roll": 3.4,
                                "yaw": 282.37,
                                "z": 731.53
                            },
                            {
                                "ImageName": "DSC00169.JPG",
                                "lat": -23.600968899999998,
                                "lon": -48.3254929,
                                "pitch": -8.64,
                                "roll": 0.55,
                                "yaw": 20.44,
                                "z": 731.13
                            },
                            {
                                "ImageName": "DSC00170.JPG",
                                "lat": -23.600824499999998,
                                "lon": -48.32543270000001,
                                "pitch": -7.62,
                                "roll": 0.89,
                                "yaw": 21.14,
                                "z": 730.95
                            },
                            {
                                "ImageName": "DSC00171.JPG",
                                "lat": -23.6006714,
                                "lon": -48.325367299999996,
                                "pitch": -7.33,
                                "roll": 0.62,
                                "yaw": 21.51,
                                "z": 730.76
                            },
                            {
                                "ImageName": "DSC00172.JPG",
                                "lat": -23.600525899999997,
                                "lon": -48.32530429999999,
                                "pitch": -7.7,
                                "roll": 0.6,
                                "yaw": 21.51,
                                "z": 730.56
                            },
                            {
                                "ImageName": "DSC00173.JPG",
                                "lat": -23.6003747,
                                "lon": -48.325238899999995,
                                "pitch": -7.59,
                                "roll": 0.73,
                                "yaw": 21.64,
                                "z": 730.25
                            },
                            {
                                "ImageName": "DSC00174.JPG",
                                "lat": -23.6002235,
                                "lon": -48.325173,
                                "pitch": -8.1,
                                "roll": 0.65,
                                "yaw": 21.61,
                                "z": 729.89
                            },
                            {
                                "ImageName": "DSC00175.JPG",
                                "lat": -23.6000838,
                                "lon": -48.325112,
                                "pitch": -7.88,
                                "roll": 0.56,
                                "yaw": 21.34,
                                "z": 729.37
                            },
                            {
                                "ImageName": "DSC00176.JPG",
                                "lat": -23.5999332,
                                "lon": -48.3250464,
                                "pitch": -7.82,
                                "roll": 0.84,
                                "yaw": 21.53,
                                "z": 728.65
                            },
                            {
                                "ImageName": "DSC00177.JPG",
                                "lat": -23.599794,
                                "lon": -48.324986100000004,
                                "pitch": -7.46,
                                "roll": 0.87,
                                "yaw": 21.85,
                                "z": 727.93
                            },
                            {
                                "ImageName": "DSC00178.JPG",
                                "lat": -23.599644100000003,
                                "lon": -48.3249208,
                                "pitch": -7.43,
                                "roll": 1.05,
                                "yaw": 21.54,
                                "z": 727.2
                            },
                            {
                                "ImageName": "DSC00179.JPG",
                                "lat": -23.5995005,
                                "lon": -48.3248578,
                                "pitch": -7.78,
                                "roll": 0.57,
                                "yaw": 21.43,
                                "z": 726.46
                            },
                            {
                                "ImageName": "DSC00180.JPG",
                                "lat": -23.599355399999997,
                                "lon": -48.324794700000005,
                                "pitch": -8.11,
                                "roll": 0.43,
                                "yaw": 21.48,
                                "z": 725.72
                            },
                            {
                                "ImageName": "DSC00181.JPG",
                                "lat": -23.5992093,
                                "lon": -48.324731400000005,
                                "pitch": -6.59,
                                "roll": 0.79,
                                "yaw": 21.63,
                                "z": 725.29
                            },
                            {
                                "ImageName": "DSC00182.JPG",
                                "lat": -23.599064399999996,
                                "lon": -48.3246683,
                                "pitch": -3.73,
                                "roll": 0.34,
                                "yaw": 21.74,
                                "z": 725.14
                            },
                            {
                                "ImageName": "DSC00183.JPG",
                                "lat": -23.5989228,
                                "lon": -48.3246075,
                                "pitch": 0.82,
                                "roll": 0.77,
                                "yaw": 21.95,
                                "z": 724.91
                            },
                            {
                                "ImageName": "DSC00184.JPG",
                                "lat": -23.5987883,
                                "lon": -48.324549700000006,
                                "pitch": 2.99,
                                "roll": 0.85,
                                "yaw": 22.21,
                                "z": 724.65
                            }
                        ]
                    }
                }
            ],
            "partial_groves": [],
            "non_valid_polygons": []
        }
    },
    "MissionType": "Mapping",
    "FlightDiscoveryId": "52759ce8-d2a9-45fb-8a37-64205efa6cf8",
    "message": "",
    "request_id": "52759ce8-d2a9-45fb-8a37-64205efa6cf8",
    "status": "pass",
    "data": {
        "message": ""
    },
    "traceback": ""
}