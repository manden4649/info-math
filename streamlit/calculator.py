import streamlit as st

#SOSU~(ほぼコピペなのであまり理解してない)
def page1():
    result1: str =''

    pflag = 1
    st.header('素数判定')
    a: int = st.number_input(label='数値を入力', value=0)
    if a >= 2:
        if st.button('計算する'):
        
            def bunkai(num):
               divisors = {}
               for prime in range(2, num + 1):
                   expon = 0
                   while (num % prime) == 0:
                       expon += 1
                       num //= prime
                   if expon != 0:
                       divisors[prime] = expon
               return divisors

               #calculation
            for i in range(2,a):
               if a % i == 0:
                   pflag = 0
                   st.info(str(i) + 'で割れるよ')
                   list = bunkai(a)
                   for i in list:
                       result1 = result1 + str(i) + '^' + str(list[i]) + '×'
                   break

            if pflag == 1:
               st.info('素数です')
            st.latex(result1[:-1])
    else:
        st.error('2以上の自然数をいれてください〜')#ERROR msg

#Euclid
def page2():
        result = ''
        a = []
        b = []
        q = []
        r = []
        st.header('ユークリッドの互除法')
        #input
        a.append(st.number_input(label='[ ]x', value=0))
        b.append(st.number_input(label='[ ]y', value=0))
        st.latex(str(int(a[0]))+'x+'+str(int(b[0]))+'y=1') #preview
        i = 0
        if 0 < a[0] or 0 < b[0]:
            if st.button('計算する'):
                col1,col2,col3 = st.columns(3)
                i = 0
                #calculation
                with col1:
                    st.subheader('ユークリッドの互除法')
                    while True:
                        q.append(a[i] // b[i])
                        r.append(a[i] % b[i])
                        st.latex(str(a[i]) + '=' + str(b[i]) + '×'\
                        + str(q[i]) + '+' + str(r[i]))

                        if r[i] == 0:
                            break
                        a.append(b[i])
                        b.append(r[i])
                        i += 1
                    st.latex('最大公約数 = '+ str(int(b[i])))

                with col2:
                    st.subheader('不定方程式')
                    P = [''] * (i+1)
                    P[i] = 1
                    while i != 0:
                        P[i-1] =  -int(((P[i] * a[i-1])-1) / a[i])
                        st.latex('1='+str(P[i])+'×'+str(a[i-1])+'+'+str(P[i-1])+'×'+str(a[i])+'\n\n')
                        i -= 1
                with col3:
                    st.subheader('特殊解')
                    st.latex('x0='+str(P[i+1]))
                    st.latex('y0='+str(P[i]))
                    st.latex('x='+str(P[i+1])+'+'+str(a[i+1])+'t')
                    st.latex('y='+str(P[i])+'-'+str(a[i])+'t')

        else:
            st.error('0むりです') #ERROR msg


#side-bar switch
st.session_state.mode = st.sidebar.radio('Which do you like?', ['素数判定', 'ユークリッド計算機'])

#change mode
if st.session_state.mode == 'ユークリッド計算機':
    page2()
else:
    page1()

