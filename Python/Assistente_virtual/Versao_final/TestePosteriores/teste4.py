# import win32com.client as win32
# excel = win32.Dispatch('Word.Application')
#
# excel.Visible = True
# _ = input("Press ENTER to quit:")
#
# excel.Application.Quit()
#
# s = "teste"
# print("par" if "e" in s else "impar")
# s2 = [i for i in range(100)]
# teste = lambda x: x * 2
# teste2 = lambda x: "True" if x % 2 == 0 else "False"

import win32com.client as win32

outlook = win32.Dispatch('outlook.application')
email = outlook.CreateItem(0)

email.To = ''
if email.To == '':
    email.To = str(input('Para quem vai esse e-mail? '))
email.Subject = ''
if email.Subject == '':
    email.Subject = str(input('Qual o assunto do e-mail? '))

conteudo = ''
nome_arquivo = ''
anexo = fr'C:\Users\clowd\Documents\mandar-email\anexo\{nome_arquivo}'
email.Attachments.Add(anexo)


css = ''' 
<style>
.email p {
    font-size: 20px;
    font-family: Arial, Helvetica, sans-serif;
}
</style>
'''
email.HTMLBody = f'''
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1">
        {css}
        </head>

        <body>
            <section class="email">

                {conteudo}

            </section>
        </body>
    </html>
    '''
email.Send()
print('Email enviado !')
