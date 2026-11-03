from app.estructura.cola_llegada import ColaLlegada
from app.estructura.lista_alta_prioridad import ListaAltaPrioridad
from app.estructura.lista_prioridad_normal import ListaPrioridadNormal
from app.estructura.pila_atendidos import PilaAtendidos
from app.servicios.atencion_service import AtencionService
from app.servicios.consulta_service import ConsultaService
from app.servicios.registro_service import RegistroService
from app.servicios.triage_service import TriageService


class HospitalFacade:

    def __init__(self):

        cola = ColaLlegada()
        alta = ListaAltaPrioridad()
        normal = ListaPrioridadNormal()
        historial = PilaAtendidos()

        self.registro = RegistroService(cola)

        self.triage = TriageService(
            cola,
            alta,
            normal
        )

        self.atencion = AtencionService(
            alta,
            normal,
            historial
        )

        self.consulta = ConsultaService(
            cola,
            alta,
            normal,
            historial
        )