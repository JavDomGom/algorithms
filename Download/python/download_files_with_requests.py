import time
import requests

urls = [
    'https://effigis.com/wp-content/uploads/2015/02/Airbus_Pleiades_50cm_8bit_RGB_Yogyakarta.jpg',
    'https://effigis.com/wp-content/uploads/2015/02/DigitalGlobe_WorldView2_50cm_8bit_Pansharpened_RGB_DRA_Rome_Italy_2009DEC10_8bits_sub_r_1.jpg',
    'https://effigis.com/wp-content/uploads/2015/02/DigitalGlobe_WorldView1_50cm_8bit_BW_DRA_Bangkok_Thailand_2009JAN06_8bits_sub_r_1.jpg',
    'https://effigis.com/wp-content/themes/effigis_2014/img/GeoEye_GeoEye1_50cm_8bit_RGB_DRA_Mining_2009FEB14_8bits_sub_r_15.jpg',
    'https://effigis.com/wp-content/uploads/2015/02/DigitalGlobe_QuickBird_60cm_8bit_RGB_DRA_Boulder_2005JUL04_8bits_sub_r_1.jpg'
]


if __name__ == "__main__":
    total_start_time = time.time()

    for url in urls:
        file = url.split('/')[-1]
        download_start_time = time.time()
        with requests.get(url, stream=True) as response:
            if response.ok:
                with open(file, 'wb') as f:
                    response.raw.decode_content = True
                    f.write(response.raw.read())
            else:
                print(f'Something went wrong with this file: {file}')
        print(f'Request time: {response.elapsed.total_seconds()}\tDownload time: {time.time() - download_start_time}')

    print(f'\nTotal time elapsed: {time.time() - total_start_time}')
