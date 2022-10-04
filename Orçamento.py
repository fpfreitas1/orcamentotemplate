#!/usr/bin/env python
# coding: utf-8

# # Nosso primeiro código Python

# In[3]:


print("Orçamento gerado com sucesso!")


# In[4]:


print("Semana do Python na prática")
print("Eu quero muito aprender Python")
print("Empowerdata!")


# In[5]:


input("Digite a descrição do projeto: ")
input("Digite a quantidade de horas estimadas: ")
input("Digite o valor da hora trabalhada: ")
input("Digite o prazo de entrega: ")


# # Armazenando dados no Python

# In[8]:


projeto = input("Digite a descrição do projeto: ")
horas_estimadas = input("Digite a quantidade de horas estimadas: ")
hora_trabalhada = input("Digite o valor da hora trabalhada: ")
prazo = input("Digite o prazo de entrega: ")


# # Calculando valor total do projeto

# In[28]:


print(int(horas_estimadas) * int(hora_trabalhada))


# In[31]:


valor_total = int(horas_estimadas) * int(hora_trabalhada)


# In[32]:


print(valor_total)


# # Gerar PDF

# In[34]:


get_ipython().system('pip install fpdf')


# In[36]:


from fpdf import FPDF


# In[61]:


pdf = FPDF()

pdf.add_page()
pdf.set_font("Arial")

pdf.image("template.png" , x=0, y=0)
pdf.text(115, 145, projeto)
pdf.text(115, 160, horas_estimadas)
pdf.text(115, 175, hora_trabalhada)
pdf.text(115, 190, prazo)
pdf.text(115, 205, str(valor_total))

pdf.output("Orçamento.pdf")

print("Orçamento gerado com sucesso!")


# In[ ]:





# In[ ]:




