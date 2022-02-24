import requests, json, time, csv

url = 'https://www.instagram.com/graphql/query'
short_code = input('Please Enter a Short Code: ')
end_cursor = ''
count = 0
counter_file = 1
jumlah_per_file = 1000

writer = csv.writer(open(f'hasil_like/{short_code} {counter_file}.csv', 'w', newline='', encoding='utf-8'))
headers = ['Username', 'Full Name', 'Profil Pict']
writer.writerow(headers)
while 1:
    variables = {
        "shortcode":short_code,
        "first":50,
        "after":end_cursor
    }

    params = {
        'query_hash': 'd5d763b1e2acf209d62d22d184488e57',
        'variables': json.dumps(variables)
    }
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
        'cookie': 'mid=YbmlQAALAAF2djwneDiO2pMJmZ0W; ig_did=3F203811-9EA3-4351-B6A3-304E4BA83A47; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; ds_user_id=2930631309; sessionid=2930631309%3AUfMzxFhJiM4LB1%3A10; csrftoken=aobk25WwSI0J5ER93xVTD9FF4RAzdUcS; datr=wnjmYVyXWw-_ni7vGiFgdipf; shbid="14186\0542930631309\0541675570352:01f77cc626f26157f8f00314441c6c1e469edffe289d873e2b796462560bc1d07c7bb775"; shbts="1644034352\0542930631309\0541675570352:01f7be11ace648d24da67f0a6d5fa0b3e3fd8ecdf953cd09101e546792649fca11fa413d"; fbsr_124024574287414=by7_z9fEPTvK-4gC8fu6uXm3X_aN-djtpjB7tA9s8YE.eyJ1c2VyX2lkIjoiMTAwMDEyMTIxMTQ0Nzg2IiwiY29kZSI6IkFRQnQyTXBHTUlycmtlNW81REktWmNyN3Npc2JuTXB3bEpEYzZBTHVBQ0tUV3FJakxoMzUxRGJwZ01SWGpaU0gtbU9Jenl1WnEyMk1QdldNWTQwbU91MVZsVzlDSTRSVWs5OUdJNTZJVElmOTJTMzhsbEdyN3BsNXpoOXZPaG9KVTc1SXBQbUFrV0VwN2hlQW5IN0pqVmoxa3g3VFR0WElYSUFKalBwTV9jeGZDcmhYbm50VFNYZFRDWFVYNHh2NW9IMUJ4VTVGcTFwd3BlX3A5cmFYTHZIajV6eWJXUzd5V0F3VkdQSDVLRksxdlZoZ3FXNW01SFdwT2ZyVUZUUFZNcmNGY2FuSnEyalFTM1FKZWZOVHJVU01IRG9RdHowaDNWMUE5NmFCVVNGckRNcWc3RmZDM3QydnQzUlNQaE51dDlRRE8xZ01hMFNkdGlacTlObXdvT0dmIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQU9zTGp3N0R5dHhxdlVVYVBkaGkyTUNpaFpCdjRiYlRydk9razdBUXBVandETTRWNVpBVEc5dVpBWkIyUTdFS0h1empLZXg0Mk1YV1BLd2wxcDNmcXJpTnB0RmIxdWZMMHlzbFpDdTg1R3dBOE5SM2hPUlVWMDJPNEMzY2ZENWwzelpCR2N5U3lENUZHd3NyZnFUY05KSERyb1pCcmVRSklJeThqbTVZWDNaQW1wSEltcVVvRnk4WkQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY0NDEwOTU5NH0; fbsr_124024574287414=by7_z9fEPTvK-4gC8fu6uXm3X_aN-djtpjB7tA9s8YE.eyJ1c2VyX2lkIjoiMTAwMDEyMTIxMTQ0Nzg2IiwiY29kZSI6IkFRQnQyTXBHTUlycmtlNW81REktWmNyN3Npc2JuTXB3bEpEYzZBTHVBQ0tUV3FJakxoMzUxRGJwZ01SWGpaU0gtbU9Jenl1WnEyMk1QdldNWTQwbU91MVZsVzlDSTRSVWs5OUdJNTZJVElmOTJTMzhsbEdyN3BsNXpoOXZPaG9KVTc1SXBQbUFrV0VwN2hlQW5IN0pqVmoxa3g3VFR0WElYSUFKalBwTV9jeGZDcmhYbm50VFNYZFRDWFVYNHh2NW9IMUJ4VTVGcTFwd3BlX3A5cmFYTHZIajV6eWJXUzd5V0F3VkdQSDVLRksxdlZoZ3FXNW01SFdwT2ZyVUZUUFZNcmNGY2FuSnEyalFTM1FKZWZOVHJVU01IRG9RdHowaDNWMUE5NmFCVVNGckRNcWc3RmZDM3QydnQzUlNQaE51dDlRRE8xZ01hMFNkdGlacTlObXdvT0dmIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQU9zTGp3N0R5dHhxdlVVYVBkaGkyTUNpaFpCdjRiYlRydk9razdBUXBVandETTRWNVpBVEc5dVpBWkIyUTdFS0h1empLZXg0Mk1YV1BLd2wxcDNmcXJpTnB0RmIxdWZMMHlzbFpDdTg1R3dBOE5SM2hPUlVWMDJPNEMzY2ZENWwzelpCR2N5U3lENUZHd3NyZnFUY05KSERyb1pCcmVRSklJeThqbTVZWDNaQW1wSEltcVVvRnk4WkQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY0NDEwOTU5NH0; rur="PRN\0542930631309\0541675645617:01f78886f9388186be254db2055630a46fa4df75e1b6bd91ebda5296a985e1eed7efa36d"'
    }

    res = requests.get(url,params=params,headers=headers).json()

    try: users = res['data']['shortcode_media']['edge_liked_by']['edges']
    except:
        print('Wait for 20 secs')
        time.sleep(20)
        continue

    for user in users:
        if count % jumlah_per_file == 0 and count != 0:
            counter_file += 1
            writer = csv.writer(open(f'hasil_like/{short_code} {counter_file}.csv', 'w', newline='', encoding='utf-8'))
            headers = ['Username', 'Full Name', 'Profil Pict']
            writer.writerow(headers)

        username = user['node']['username']
        full_name = user['node']['full_name']
        profile_pict = user['node']['profile_pic_url']
        count += 1
        print(count,username,full_name,profile_pict)

        writer = csv.writer(open(f'hasil_like/{short_code} {counter_file}.csv', 'a', newline='', encoding='utf-8'))
        data = [username,full_name,profile_pict]
        writer.writerow(data)

    end_cursor = res['data']['shortcode_media']['edge_liked_by']['page_info']['end_cursor']
    has_next_page = res['data']['shortcode_media']['edge_liked_by']['page_info']['has_next_page']
    if has_next_page == False: break
    time.sleep(2)

