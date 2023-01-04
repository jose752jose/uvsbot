from pyobigram.utils import sizeof_fmt,nice_time
import datetime
import time
import os
from os import walk

def dashboard():
    start_msg = '💢Bienvenid@💢\n'
    start_msg += '🔰Usa /mydata para ver la configuración'
    return start_msg

def text_progres(index,max,size=21,step_size=5):
    try:
        if max<1:
            max += 1
        porcent = index / max
        porcent *= 100
        porcent = round(porcent)
        make_text = ''
        index_make = 1
        make_text += '['
        while(index_make<size):
            if porcent >= index_make * step_size:make_text+='▣'
            else:make_text+='□'
            index_make+=1
        make_text += ']'
        return make_text
    except Exception as ex:
            return ''

def porcent(index,max):
    porcent = index / max
    porcent *= 100
    porcent = round(porcent)
    return porcent

def createDownloading(filename,totalBits,currentBits,speed,time,tid=''):
    msg = '📥Descargando....[' + str(porcent(currentBits, totalBits)) + '%]\n\n'
    msg += '📄Name: ' + filename + '\n'
    msg += text_progres(currentBits, totalBits) + '\n'
    #msg += '💯Porcentaje: \n'
    #msg += '📂Total: \n\n'
    msg += '📥Descargado: ' + sizeof_fmt(currentBits) + ' -- ' + sizeof_fmt(totalBits) + '\n'
    msg += '⚡Speed: ' + sizeof_fmt(speed) + '/s || ETA: ' + str(datetime.timedelta(seconds=int(time))) + 's\n\n'
  #  msg += '🕛Tiempo: \n\n'
    return msg
def createUploading(filename,totalBits,currentBits,speed,time,originalname=''):
    msg = '📤Subiendo... [' + str(porcent(currentBits, totalBits)) + '%]'
    msg += '\n📄Nombre: ' + filename + '\n'
    if originalname != '':
        msg = str(msg).replace(filename, originalname)
        msg += '📄Nombre: ' + str(filename) + '\n'
    msg += text_progres(currentBits, totalBits) + '\n'
   # msg += '💯Porcentaje: \n\n'
  #  msg += '📂Total: ' + sizeof_fmt(totalBits) + '\n'
    msg += '📤Subido: ' + sizeof_fmt(currentBits) + ' -- ' + sizeof_fmt(totalBits) + '\n'
    msg += '⚡Speed: ' + sizeof_fmt(speed) + '/s\n'
  #  msg += '🕛Tiempo: ' + str(datetime.timedelta(seconds=int(time))) + 's\n\n'
    return msg
def createCompresing(filename,filesize,splitsize):
    msg = '🗜️Comprimiendo... \n'
    msg+= '📄Nombre: ' + str(filename)+'\n'
    msg+= '📂Tamaño: ' + str(sizeof_fmt(filesize))+'\n'
    msg+= '🗜️Tamaño Partes: ' + str(sizeof_fmt(splitsize))+'\n'
    msg+= '📚Partes: ' + str(round(int(filesize/splitsize)+1,1))+'\n\n'
    return msg
def createFinishUploading(filename,filesize,datacallback=None):
    msg = '≪═══❖• ° •❖═══≫\nᎪᎡᏟᎻᏆᏙϴ ՏႮᏴᏆᎠϴ\n≪═══❖• . •❖═══≫\n\nꋊꄲꂵꃳꋪꏂ:' + str(filename)+ f'\nԵαตαղ̃օ: {str(sizeof_fmt(filesize))}\n'
    if datacallback:
       msg += 'datacallback: ' + datacallback
    return msg

def createFileMsg(filename,files):
    import urllib
    if len(files)>0:
        msg= '<b>ꏂꋊ꒒ꋬꉔꏂꇙ</b>\n'
        for f in files:
            url = urllib.parse.unquote(f['directurl'],encoding='utf-8', errors='replace')
            #msg+= '<a href="'+f['url']+'">🔗' + f['name'] + '🔗</a>'
            msg+= "<a href='"+url+"'>🔗"+f['name']+'🔗</a>\n'
        return msg
    return ''

def createFilesMsg(evfiles):
    msg = '📑Archivos ('+str(len(evfiles))+')📑\n\n'
    i = 0
    for f in evfiles:
            try:
                fextarray = str(f['files'][0]['name']).split('.')
                fext = ''
                if len(fextarray)>=3:
                    fext = '.'+fextarray[-2]
                else:
                    fext = '.'+fextarray[-1]
                fname = f['name'] + fext
                msg+= '/txt_'+ str(i) + ' /del_'+ str(i) + '\n' + fname +'\n\n'
                i+=1
            except:pass
    return msg

def files(username, path):
    listado=os.listdir(path)
    dir, subdirs, archivos = next(walk(path))
    sms = f'🆔Sesión: @{username}\n'
    sms += f'≪═══❖• Mɪs Aʀᴄʜɪᴠᴏs {str(len(listado))} •❖═══≫\n'
    sn = -1
    for s in subdirs:
        sn += 1
        sms +=f'\n/cdir_{sn} 📁 {s}'
    an = -1
    for a in archivos:
        an += 1
        size=(a,os.stat(os.path.join(path, a)).st_size)
        size=(size[1] / 1024 / 1024)
        sms +=f'\n╭◆ ❮ /up_{an} ❯-❮ /rm_{an} ❯-❮ /split_{an}_100 ❯'
        sms +=f'\n├◆{an} - {a}'
        sms +=f'\n╰◆📦{str(size)[:4]}MB\n'
       # sms += f'🆔Sesión: @{username}\n\n'
    return sms

def createStat(username,userdata,isadmin):
    from pyobigram.utils import sizeof_fmt
    msg = '🆔ѕєѕιόи: @' + str(username)+'\n'
    msgAdmin = '🚫'

    if isadmin:
        msgAdmin = '✅'
    msg+= '👤⚡Admin: ' + msgAdmin + '\n'
    proxy = '🚫'
    if userdata['proxy'] !='':
       proxy = '✅'
    msg+= '🛰️Proxy: ' + proxy + '\n'
    autoup = '✔️'
    if userdata['autoup'] == 1:
        autoup = '✅'
    msg += '📤Autoup: ' + autoup
    return msg
