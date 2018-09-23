while True:
        tang =int(input())
        if tang == 0:
                break
        else:
                tax = 0.0
                if tang > 10000000:
                        taxcal = (tang-10000000)*0.32
                        tax = tax + taxcal
                        tang = 10000000
                if tang > 5000000:
                        taxcal = (tang-5000000)*0.2
                        tax = tax + taxcal
                        tang = 5000000
                if tang > 1000000:
                        taxcal = (tang-1000000)*0.12
                        tax = tax + taxcal
                        tang = 1000000
                if tang > 100000:
                        taxcal = (tang-100000)*0.06
                        tax = tax + taxcal
                print (int(tax))
