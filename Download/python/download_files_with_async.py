import time
import aiofiles
from aiohttp.client import ClientSession
from asyncio import Semaphore, gather, run, wait_for


urls = [
    'https://effigis.com/wp-content/uploads/2015/02/Airbus_Pleiades_50cm_8bit_RGB_Yogyakarta.jpg',
    'https://effigis.com/wp-content/uploads/2015/02/DigitalGlobe_WorldView2_50cm_8bit_Pansharpened_RGB_DRA_Rome_Italy_2009DEC10_8bits_sub_r_1.jpg',
    'https://effigis.com/wp-content/uploads/2015/02/DigitalGlobe_WorldView1_50cm_8bit_BW_DRA_Bangkok_Thailand_2009JAN06_8bits_sub_r_1.jpg',
    'https://effigis.com/wp-content/themes/effigis_2014/img/GeoEye_GeoEye1_50cm_8bit_RGB_DRA_Mining_2009FEB14_8bits_sub_r_15.jpg',
    'https://effigis.com/wp-content/uploads/2015/02/DigitalGlobe_QuickBird_60cm_8bit_RGB_DRA_Boulder_2005JUL04_8bits_sub_r_1.jpg'
]

MAX_TASKS = 5
MAX_TIME = 60


async def download(urls):
    tasks = []
    sem = Semaphore(MAX_TASKS)

    async with ClientSession() as sess:
        for url in urls:
            file = url.split('/')[-1]
            tasks.append(
                wait_for(
                    download_one(url, sess, sem, file),
                    timeout=MAX_TIME,
                )
            )

        return await gather(*tasks)


async def download_one(url, sess, sem, dest_file):
    async with sem:
        print(f'Downloading: {url}')

        async with sess.get(url) as response:
            content = await response.read()

        if response.status != 200:
            print(f'Download failed: {response.status}')
            return

        async with aiofiles.open(dest_file, '+wb') as f:
            await f.write(content)


if __name__ == '__main__':
    total_start_time = time.time()

    run(download(urls))

    print(f'\nTotal time elapsed: {time.time() - total_start_time}')
