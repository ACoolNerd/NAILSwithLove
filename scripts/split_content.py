#!/usr/bin/env python3
import json
import os
import re

def generate_marketing_content():
    print("Extracting and compiling marketing content templates...")
    
    # We will define a structured list of marketing and outreach templates
    # directly matching Yesenia's playbook and startup plan.
    content = {
        "ads": [
            {
                "title": "Anuncio 1: Primera Cita Boutique (Manicure Semipermanente)",
                "hook": "🌟 Uñas boutique hechas con amor, en la comodidad de tu hogar.",
                "body": "¡Hola Cali! ✨ Disfruta de un manicure semipermanente premium con diseño sencillo por solo COP $55.000. Cuidado profesional, higiene visible y la comodidad de no tener que salir de casa.",
                "cta": "📲 Toca el botón para ver disponibilidad y agendar por WhatsApp.",
                "tags": "#NailsCali #ManicureADomicilio #UñasBoutique #CaliValle"
            },
            {
                "title": "Anuncio 2: Promo de Referidos (Amigas y Autocuidado)",
                "hook": "💅 Compartir el amor por las uñas tiene recompensa.",
                "body": "Recomienda Nails with Love by Yesenia a una amiga. Cuando ella agende su primera cita boutique, ¡ambas recibirán un 15% de descuento en su próximo servicio! Válido para manicure semipermanente o extensiones.",
                "cta": "💬 Escríbeme por WhatsApp con el nombre de tu recomendada para activar tu descuento.",
                "tags": "#ReferidosNails #UñasCali #AmigasCali #BellezaADomicilio"
            },
            {
                "title": "Historia 3: Agenda tu Cita / Reserva Fácil",
                "hook": "⏰ ¿Uñas perfectas esta semana? Es muy fácil agendar.",
                "body": "Nails with Love by Yesenia te ofrece citas a domicilio y en home-boutique con precios claros desde el primer momento. Sin sorpresas, higiene 100% garantizada en cada herramienta.",
                "cta": "👉 Desliza o toca el enlace para chatear directamente conmigo en WhatsApp.",
                "tags": "#NailsWithLove #NailArtCali #AgendaTuCita #UñasPerfectas"
            }
        ],
        "whatsapp_flows": [
            {
                "stage": "1. Saludo Inicial / Consulta",
                "trigger": "Mensaje automático desde ad/link",
                "template": "¡Hola Yesenia! ✨ Quiero conocer tus servicios y agendar una cita. ¿Me compartes el menú y disponibilidad para esta semana? Gracias."
            },
            {
                "stage": "2. Respuesta y Menú",
                "trigger": "Primer contacto de Yesenia",
                "template": "¡Hola! Qué gusto saludarte. Soy Yesenia de Nails with Love. 💖 Con gusto te comparto nuestro menú de servicios:\n\n• Manicure Semipermanente (Diseño sencillo incluido): COP $55.000 (Primera cita boutique)\n• Extensiones de Uñas (Gel X / Acrílico): Desde COP $120.000\n• Retiro semipermanente (otra manicurista): COP $10.000\n\n¿Qué servicio te gustaría agendar y en qué barrio te encuentras?"
            },
            {
                "stage": "3. Solicitud de Datos y Anticipo",
                "trigger": "Barrio y servicio confirmados",
                "template": "¡Perfecto! Para confirmar tu cita en [Barrio] para el [Día] a las [Hora], solicitamos un anticipo del 50% (COP $[Monto]) a través de Nequi al celular 3108486630.\n\nUna vez realizado, por favor envíame el comprobante por este medio para bloquear tu espacio. ¡Muchas gracias por tu confianza!"
            },
            {
                "stage": "4. Confirmación de Reserva",
                "trigger": "Comprobante de Nequi recibido",
                "template": "¡Recibido! Tu cita queda confirmada para el [Día] a las [Hora] en [Dirección]. Te enviaré un recordatorio el día anterior. ¡Nos vemos pronto para consentir tus uñas con mucho amor! 💅✨"
            },
            {
                "stage": "5. Recordatorio Día Anterior",
                "trigger": "24 horas antes de la cita",
                "template": "¡Hola! Te saluda Yesenia. 🌸 Te recuerdo que mañana a las [Hora] tenemos tu cita de uñas en [Dirección]. Por favor confírmame que todo sigue en pie. ¡Que tengas un lindo día!"
            }
        ],
        "outreach_templates": [
            {
                "channel": "Instagram DM - Alianzas con Spas/Peluquerías",
                "target": "Salones de belleza o spas en Cali que no ofrecen manicure",
                "template": "¡Hola [Nombre del Salón/Administradora]! Un gusto saludarte. Soy Yesenia de Nails with Love, una boutique de uñas a domicilio aquí en Cali. 💅\n\nHe visto el excelente trabajo que hacen en [Servicios que ofrecen, ej: cabello/cejas], y me encantaría proponerte una alianza sencilla. Muchos clientes buscan servicios de uñas mientras se atienden con ustedes, y nosotros podríamos ofrecerles cobertura a domicilio bajo un sistema de referidos con comisión del 10% para ustedes por cada cliente agendado.\n\n¿Te interesaría que te visite esta semana para compartirte nuestras tarjetas y coordinar? ¡Muchas gracias!"
            },
            {
                "channel": "WhatsApp / Instagram DM - Reclutamiento de Recién Graduadas",
                "target": "Graduadas de Academias de Belleza de Cali",
                "template": "¡Hola [Nombre]! Te saluda Yesenia de Nails with Love. 🌸 Vimos tu portafolio y nos encanta el nivel de detalle y pasión en tus diseños.\n\nEstamos expandiendo nuestro servicio de uñas boutique a domicilio en Cali y buscamos manicuristas recién graduadas que quieran crecer con nosotros, ganar experiencia práctica y trabajar en un ambiente flexible con excelentes comisiones y capacitación constante en bioseguridad.\n\nSi te interesa conocer más sobre la vacante y nuestro esquema de trabajo, me encantaría programar una breve charla por WhatsApp esta semana. ¿Qué día te queda mejor?"
            }
        ]
    }
    
    # Optional check: read client-growth-playbook.md to extract text lines
    playbook_path = "/Users/ACoolNERD/Documents/NAILS with Love by YESENIA/client-growth-playbook.md"
    if os.path.exists(playbook_path):
        print(f"Reading {os.path.basename(playbook_path)} for supplementary tags...")
        with open(playbook_path, "r", encoding="utf-8") as f:
            text = f.read()
            # Find and add some key instructions as operational tips
            tips = re.findall(r"-\s+(?:\*\*)?([A-Z][a-zA-Z\s,;.:ñíáéóú]+)(?:\*\*)?", text)
            if tips:
                content["operational_tips"] = [t.strip() for t in tips[:12]]
                
    # Save directory setup
    target_dir = "/Users/ACoolNERD/Documents/NAILS with Love by YESENIA/launch-system-9.7/website/dashboard/data"
    os.makedirs(target_dir, exist_ok=True)
    
    output_path = os.path.join(target_dir, "marketing_content.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(content, f, ensure_ascii=False, indent=2)
        
    print(f"Marketing content templates saved to: {output_path}")

if __name__ == "__main__":
    generate_marketing_content()
