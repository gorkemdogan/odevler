def get_signal_type(signal):
    if(signal>=0 and signal <=50):
        return 'Çok Zayıf Signal'
    elif(signal>=51 and signal <=100):
        return 'Zayıf Signal'
    elif(signal>=101 and signal <=150):
        return 'Orta Signal'
    elif(signal>=151 and signal <=200):
        return 'Güçlü Signal'
    else:
        return 'Çok Güçlü Signal'

def get_device_type(type):
    if(type ==1):
        return 'Televizyon'
    elif(type==2):
        return 'Çamaşır Makinesi'
    elif(type==3):
        return 'Buzdolabı'
    else:
        return 'Fırın'

def get_device_status(status):
    if(status == 1):
        return 'On'
    else:
        return 'Off'
def get_response_status(status):
    if(status == 1):
        return 'Cevap isteniyor'
    else:
        return 'Cevap istenmiyor'

def get_code_type(type):
    if(type == 'send'):
        return 'Giden'
    else:
        return 'Gelen'



def decode(string):
    signals = string.split('\n')
    signals = ' '.join(signals).split()
    print(signals)
    for index,signal in enumerate(signals):
        parts = signal.split('-')
        if(parts[0] == 'receive' or parts[0] == 'send'):
            if((len(parts[1:])==3 and parts[0] == 'receive') or (len(parts[1:])==4 and parts[0] =='send')):
                #parts checked
                if(int(parts[1])>=0 and int(parts[1])<=255):
                    #Sİnyal kurala uyuyor
                    if(int(parts[2])>=1 and int(parts[2])<=4):
                        #cihaz tipi kurala uyuyor
                        if(int(parts[3])==0 or int(parts[3])==1):

                            #durum kurala uyyor
                            print('Kod tipi : {} - {}'.format(parts[0],get_code_type(parts[0])))
                            print('Sinyal gücü : {} - {} '.format(parts[1],get_signal_type(int(parts[1]))))
                            print('Cihaz : {} - {}'.format(parts[2],get_device_type(int(parts[2]))))
                            print('Durumu : {} - {}'.format(parts[3],get_device_status(int(parts[3]))))
                            if(parts[0]=='send' and parts[4]):
                                print('Cevap : {} - {}'.format(parts[4],get_response_status(int(parts[4]))))

                        else:
                            print('Durum kurala uymuyor')
                    else:
                        #out of rule
                        print('Cihaz tipi kurala uymuyor')
                else:
                    print('Signal aralığı kurala uymuyor')

            else:
                print('Olması gereken eleman kuralına uymuyor')
        else:
            print('Sender veya Receiver ile başlamalıdır')

        if(index<len(signals)-1):
            print('---------------------------')


decode('send-245-3-1-1\nreceive-4-1-0\nsend-100-6-0-0')



