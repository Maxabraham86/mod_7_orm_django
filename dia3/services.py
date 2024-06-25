from dia3.models import Tarea , SubTarea



def crear_tarea (*descripciones: str):
    for descripcion in descripciones:
        t = Tarea(descripcion=descripcion)
        t.save()
    imprimir_en_pantalla()
    
def recupera_tareas_y_subtareas():
    tareas = Tarea.objects.filter(eliminada=False)
    return tareas

def recupera_tareas(idtarea):
    t= Tarea.objects.get(id=idtarea)
    t.eliminada = False
    t.save()
    
def crear_nueva_tarea():
    pass

def crear_sub_tarea(descripcion: str, idtareas :int):
    t= Tarea.objects.get(id=idtareas)
    st = SubTarea(descripcion =descripcion, tarea = t)
    st.save()

def eliminar_tarea(idtarea):
    t = Tarea.objects.get(id=idtarea)
    t.eliminada = True
    t.save()

def elminar_sub_tarea( idsubtarea: int):
    t = Tarea.objects.get(id=idsubtarea)
    t.eliminada = True
    t.save()


def imprimir_en_pantalla():
    tareas = recupera_tareas_y_subtareas()
    for t in tareas:
        print (f'[{t.id}]  {t.descripcion}')
        # if t.subtareas:
        #     import pdb ; pdb.set_trace()
        for sub_tarea in t.subtareas.filter(eliminada=False):
            print (f'       {sub_tarea.id} {sub_tarea.descripcion}')