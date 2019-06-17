class Util:

    ANCHO= 640
    ALTO= 480
    NEGRO=[0,0,0]

    def cortar(img,an_cor,al_cor):
        m=[]
        for h in range(0,10):
            ls=[]
            for i in range(0,7):
                cuadro = img.subsurface(i*an_cor,h*al_cor,an_cor,al_cor)
                ls.append(cuadro)
            m.append(ls)

        return m