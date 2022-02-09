import tc.er as er
#Implementação da tarefa AC, Aluno: Pedro Castro

# Vamos cadastrar Expressões Regulares para serem retornadas como texto pelo método printw(), as expressões estão ordenadas com crescimento de complexidade para mostrar a capacidade a função em converter o código da ER para texto

exp1 = ('',0)
exp2 = ('*',1)
exp3 = ('+',1,0)
exp4 = ('*',('+',1,0))
exp5 = ('*',0,1)
exp6 = ('*',('+',1,0))
exp7 = ('',('*',('+',0,1)),1)
exp8 = ('',('*',1),('*',('+',0,1)))
exp9 = ('',('*',('+',0,1),('',0)),1)
exp10 = ('',('*',('+',0,1),('*',1,0)),1)

exp = [exp1,exp2,exp3,exp4,exp5,exp6,exp7,exp8,exp9,exp10]

def mostrar_ER():
  for estado in exp:
    print(er.printw(estado))