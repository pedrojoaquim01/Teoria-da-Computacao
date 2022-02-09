import tc.er as er

#Implementação da tarefa AD, Aluno: Pedro Castro
# ER: 1*(0+1)*0*

exp = ('',('*',1),('*',('+',0,1)))

afn_esperada = ({'f1', 'f2', 'f3', 'f4', 'f5', 'i1', 'i2', 'i3', 'i4', 'i5'},{0, 1},{('f1', ''): {'f3'},('f2', ''): {'f3'},('f3', ''): {'f5', 'i3'},('f4', ''): {'i5'},('i1', 0): {'f1'},('i2', 1): {'f2'},('i3', ''): {'i1', 'i2'},('i4', ''): {'f4', 'i1'},('i5', ''): {'f5', 'i3'}},'i4',{'f5'})

er_para_afn_esperada = ({'f10', 'f11', 'f6', 'f7', 'f8', 'f9', 'i10', 'i11', 'i6', 'i7', 'i8', 'i9'},{0, 1},{('f10', ''): {'f11', 'i10'},('f6', ''): {'f7', 'i6'},('f7', ''): {'i11'},('f8', ''): {'f10'},('f9', ''): {'f10'},('i10', ''): {'i8', 'i9'},('i11', ''): {'f11', 'i10'},('i6', 1): {'f6'},('i7', ''): {'f7', 'i6'},('i8', 0): {'f8'},('i9', 1): {'f9'}},'i7',{'f11'})

def criar_afn():
  #Criamos as bases
  base0 = er.er2afn_base(0)  
  base1 = er.er2afn_base(1)

  #Realizamos a união utilizando as bases criadas
  union = er.er2afn_union(base1,base0)

  #Realizamos o Kleene
  r = er.er2afn_kleene(base0)
  s = er.er2afn_kleene(union)

  #É feita a concatenação
  afn = er.er2afn_concat(r,s)

  #Retornamos a AFN gerada
  return afn

def teste_afn():
  return criar_afn(),afn_esperada, "É possível ver a mestra estrutura entre os dois"

def teste_er_para_afn():
  return er.er2afn(exp),er_para_afn_esperada, "É possível ver a mestra estrutura entre os dois"