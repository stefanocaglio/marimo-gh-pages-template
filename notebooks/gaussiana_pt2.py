import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # **La funzione gaussiana (parte 2)**

    In questo laboratorio vedremo come creare dei grafici con lo scopo di costruire la funzione gaussiana e capire il suo comportamento.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## **Librerie utilizzate**

    Iniziamo importando le librerie che utilizzeremo

    ```python
    import marimo as mo
    import matplotlib.pyplot as plt
    import math
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import matplotlib.pyplot as plt
    import math
    return math, mo, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## **Creare gli elementi del grafico**

    Esattamente come quando creaiamo un grafico a mano, abbiamo bisogno di **creare un elenco di coordinate $x$ e $y$** per poter posizionare i punti sul piano cartesiano.

    Le $x$, le *ascisse*, vengono anche chiamate anche *variabili indipendenti* perché siamo liberi di sceglierne i valori per la rappresentazione. Chiaramente i valori che scegliamo devono rispettare le *condizioni di esistenza* della funzione che dobbiamo rappresentare, ovvero quelle considizioni che garantiscono che la funzione esista, sia calcolabile, abbia "senso".

    Le $y$, le *ordinate*, vengono chiamate anche *variabili dipendenti* in quanto il loro valore *dipende* dalla $x$ scelta **e** dalla funzione che stiamo considerando: il loro valore, quindi, non può variare liberamente, ma è vincolato da questi due apetti.


    ### **Creare la lista delle ascisse**

    Ora iniziamo a creare e a popolare la lista che contiene i valori ascisse $x$ per le quali sarà calcolata la funzione. Dobbiamo: 

     - creare una lista vuota;
     - **definire il domino**: significa impostare la $x$ minima e massima da visualizzare. Nel caso, invece, di funzioni definite non in tutto $\R$, per tenere conto di eventuali condizioni di esistenza devo eliminare dalla lista $x$ i valori esclusi.<br/> A questo scopo posso utilizzare la funzione `x.drop(0)`, per esempio, per eliminare il valore $0$ dalla lista $x$. Il metodo `drop` elimina solo la prima occorrenza dell'elemento riportato fra parentesi e questo a va bene dato che la lista $x$ è stata costruita in modo tale che i valori siano crescenti.
     - scegliere in quanti segmenti $n$ discretizzare il dominio;
     - calcolare la lunghezza di ogni singolo segmento di discretizzazione (lo step o distanza fra un punto e l'altro!);
     - riempire la lista delle $x$ usando un metodo a scelta. Per chiarezza si può usare un ciclo `for` che esegue $n+1$ cicli (perché i punti sono uno in più del numero di segmenti di discretizzazione) e aggiungere al valore della $x_{min}$ ogni volta uno step, aiutandomi con il contatore del ciclo. Il valore calcolato viene aggiunto alla lista tramite il metodo `.append()`.


    ```python
    x = []

    x_min = -4.0
    x_max = 4.0
    n = 1000  # Passi di discretizzazione
    step = (x_max - x_min) / n

    for i in range(n + 1):
        x.append(x_min + i * step)
    ```

    ### **Creare la lista delle ordinate**

    Una volta creata la lista che contiene le ascisse, creare e popolare la lista delle ordinate è semplice. Basta: 
    - creare una lista vuota
    - riempire la lista usando la definizione della funzione e il metodo `.append()`.

    ```python
    y = []

    for i1 in range(n + 1):
        y.append(math.e ** (-(x[i1] ** 2)))
    ```


    ### **Alcune osservazioni**

    1. Da un punto di vista computazionale, converrebbe calcolare i valori delle $y$ direttamente nel ciclo `for` con cui abbiamo riempito la lista delle $x$. In questa spiegazione si sono usati due cicli per chiarezza espositiva ma il codice che effettivamente crea i grafici seguenti usa un solo ciclo.
    2. In *marimo*🌊🍃 tutte le variabili dichiarate nelle varie celle sono considerate **variabili globali**, per poter garantire che i notebook di *marimo*🌊🍃 siano ***interattivi*** (ci possiamo interagire), ***reattivi*** (rispondano alle modifiche) e ***riproducibili*** (possano essere eseguiti da tutti allo stesso modo). Per questo motivo **i nomi delle variabili globali devono essere unici** in tutto il notebok. <br/>Se sono necessarie delle variabili locali, come per esempio i contatori nei cicli, questo possono essere definite iniziando il nome della variabile con il simbolo underscore `_`. Per esempio posso usare in più celle la variabile `_i` in quato viene definita localmente, cioè solo all'interno della cella. Al suo esterno questa variabile non è visibile e quindi ilsuo nome può essere usato di nuovo.
    3. Per creare le liste di $x$ e $y$ esistono modi più rapidi che saranno affrontati più avanti. Da un punto di vista didattico conviene, per la comprensione del processo di costruzione sia della conoscenza sia dei grafici oggetto di queste lezioni, fare esperienza con i costrutti base del linguaggio Python che stiamo utlizzando.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## **Creare il grafico**

    Ora che abbiamo i punti che compongono il grafico, possiamo creare il grafico: per questo utilizziamo la libreria `matplotlib.pyplot` che permette di creare tutti gli aspetti del grafico: linee, assi, griglia, titolo, legenda.

    Il codice necessario è il seguente:

    ```python
    plt.figure()
    plt.plot(x, y1, label=r"$y= e^{-x^2}$")
    plt.title(r"Grafico della funzione $y= e^{-x^2}$")
    plt.grid()
    plt.legend()
    plt.gca()
    ```

    Da notare che, se si vogliono utilizzare le formule scritte utilizzando il linguaggio $\LaTeX$, le stringhe dei titoli e dei contenuti delle legende devono essere precedute dalla lettera `r`. Questa significa *raw*, ovvero che la stringa che segue deve essere trattata dall'interprete di Python letteralmente, in particolare il carattere *backslash* `\`. Questo è necessario in quanto i comandi di linguaggio $\TeX$ che devono essere interpretati iniziano tutti con il catattere `\`.
    """
    )
    return


@app.cell
def _(math, plt):
    x = []

    x_min = -4.0
    x_max = 4.0
    n = 1000  # Passi di discretizzazione
    step = (x_max - x_min) / n

    y1 = []

    for i1 in range(n + 1):
        x.append(x_min + i1 * step)
        y1.append(math.e ** (-(x[i1] ** 2)))

    plt.figure()
    # fig, ax = plt.subplots()
    plt.grid()
    plt.title(r"Grafico della funzione $y= e^{-x^2}$")
    plt.plot(x, y1, label=r"$y= e^{-x^2}$")
    plt.legend()
    plt.gca()
    return n, x, y1


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## **Rendiamo interattivo il grafico!**

    Prima abbiamo creato il grafico della funzione $y= e^{-x^2}$: ora, usando la possibilità date da *marimo*🌊🍃, proviamo a rendere interattivo il grafico con l'obiettivo di capire come può variare in base a tre parametro che possiamo inserire per rendere la funzione la più generale possibile. 

    Possiamo pensare di vole graficare la seguente funzione:

    $$y= A e^{-B{(x-C)}^2} $$

    Per ottenere la funzione che abbiamo graficato prima, si devono sostituire i valori $A=1$ $B=1$ e $C=0$. Questa funzione rimarrà visibile.

    Prova a modificare i valori dei parametri $A$, $B$ e $C$ per capire il loro effetto sulla funzione generale.

    Nota che, per l'applicazione di nostro interesse, deve essere:

     - $A>0$
     - $B>0$
     - $C \in \mathbb{R}$
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    A = mo.ui.slider(start=0.1, stop=5, step=0.1, label="A", value=1)
    B = mo.ui.slider(start=0.1, stop=5, step=0.1, label="B", value=1)
    C = mo.ui.slider(start=-5, stop=5, step=0.5, label="C", value=0)
    button = mo.ui.run_button(label="Clicca per aggiornare")
    return A, B, C, button


@app.cell(hide_code=True)
def _(A, B, C, button, mo):
    mo.vstack([A, B, C, button])
    return


@app.cell(hide_code=True)
def _(A, B, C, button, math, mo, n, plt, x, y1):
    mo.stop(not button.value, mo.md("Clicca il tasto qui sopra ⇧ per rigenerare il grafico con i nuovi valori selezionati!"))

    y3 = []

    for _i in range(n + 1):
        y3.append(A.value*math.e**(-B.value*(x[_i]-C.value)**2))

    plt.figure()
    plt.grid()
    plt.title(r'Funzioni gaussiane')
    plt.plot(x,y1,label=r'$y= e^{-x^2}$')
    if C.value>=0:
        stringa = r'$y= {:.1f}\, e^{{-{:.1f}\, (x-{:.1f})^2}} $'.format(A.value,B.value,C.value)
    else:
            stringa = r'$y= {:.1f}\, e^{{-{:.1f}\, (x+{:.1f})^2}} $'.format(A.value,B.value,-C.value)
    # print(stringa)
    plt.plot(x,y3,label=stringa)
    plt.legend()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Il parametro A

    Il parametro $A$ è un parametro che modifica l'**altezza**, o ampiezza, della curva:

    - se $A>1$ la curva viene amplificata
    - se $0<A<1$ la curva viene contratta


    ### Il parametro B

    Il parametro $B$ è un parametro che modifica la **larghezza** della forma a campana:

    - se $B>1$ la campana si stringe
    - se $0<B<1$ la campana viene allargata


    ### Il parametro C

    Il parametro $C$, invece, è un parametro che modifica la **posizione** della curva. Si tratta di una traslazione lungo l'asse $x$ per cui:

    - se $C>0$ la curva viene traslata verso destra
    - se $C<0$ la curva viene traslata verso sinistra
    """
    )
    return


@app.cell
def _(mo):
    mo.sidebar(
        [
            mo.md("**La gaussiana (pt. 1)**"),
            mo.nav_menu(
                {
                    "https://stefanocaglio.com": f"{mo.icon('lucide:home')} Home",
                    "https://stefanocaglio.quarto.pub/": f"{mo.icon('lucide:user')} About",
                    # "#/contact": f"{mo.icon('lucide:phone')} Contact",
                    "Links": {
                    #    "https://twitter.com/marimo_io": "Twitter",
                        "https://github.com/marimo-team/marimo": "GitHub",
                    },
                },
                orientation="vertical",
            ),
        ]
    )
    return


if __name__ == "__main__":
    app.run()
