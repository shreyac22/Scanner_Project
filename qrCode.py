import qrcode

#taking UPI ID 
upi_id=input("Enter your UPI ID = ")

phonePe_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#creating qr code
phonePe_qr=qrcode.make(phonePe_url)
paytm_qr=qrcode.make(paytm_url)
google_pay_qr=qrcode.make(google_pay_url)

#save qr code
phonePe_qr.save('phonePe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

#display qr code
phonePe_qr.show()
paytm_qr.show()
google_pay_qr.show()