---
name: habilidad-principios-ux
description: "Migrated skill bundle (see SKILL.md body)."
---

## Abstract

[TODO: Write abstract]

# Habilidad Principios UX Psicológicos
> Capa de asesoramiento para diseñadores y equipos de producto que aplican principios de psicología cognitiva al diseño de experiencias de usuario. Superficie principios relevantes y anti-patrones a evitar.

## Cuándo Usar

Después de definir el diseño de una página, componente o flujo, ejecuta la lente de principios UX psicológicos para encontrar qué principios estás aplicando y cuáles te están pasando por alto.

## Proceso de Decisión

1. **Identifica el tipo de página o componente** — landing, pricing, onboarding, dashboard, checkout, about/trust
2. **Extrae 3-5 principios más relevantes** de las prescripciones por tipo de página abajo
3. **Para cada principio, estatal:** qué es → cómo aplicarlo ESTE diseño específico → qué el anti-patrón se ve
4. **Pesa contra restricciones** — identidad de marca, accesibilidad y requisitos técnicos siempre toman prioridad
5. **Recomienda cambios específicos y implementables** — no consejos abstractos. Muestra qué cambiar en el markup, layout, copy o jerarquía visual. Si puedes apuntar a una línea de código o regla CSS, hazlo.

## Cómo Pesar

Los principios UX psicológicos son **una entrada entre muchas**. La jerarquía de peso:

1. **Identidad y visión de marca** (mayor — el diseño debe verse y sentirse correcto para la marca)
2. **Accesibilidad y usabilidad** (no negociable — WCAG compliance, targets táctiles, contraste)
3. **Calidad técnica** (performance, SEO, diseño responsive)
4. **Principios UX psicológicos** (esta habilidad — influencia sutil, no imposición pesada)

Nunca sacrifiques la identidad de marca o la confianza del usuario por un truco psicológico. Si un principio entra en conflicto con un buen diseño, el buen diseño gana.

## Qué Esta Habilidad No Es

- **No un manual de patrones oscuros** — cada principio aquí es aplicación UX ética solo
- **No un sistema de diseño completo** — augments habilidades de diseño existentes
- **No un reemplazo para investigación de usuarios** — datos reales de usuarios siempre superan teoría
- **No una lista rígida** — usa los principios que encajen, ignora los que no

## Principios por Tipo de Página (Inline)

### Página Principal / Landing Page

| Principio | Aplicación |
|-----------|------------|
| **First Impressions** | El hero comunica value en under 3 seconds. Formado en 50ms — no segundas oportunidades. |
| **Anchoring** | Lead with your strongest metric o claim. First number seen sets the reference. |
| **Social Proof** | Números reales visibles early (usuarios, resultados, track record). Claims vagos no convierten. |
| **Information Scent** | Navegación clara — el usuario sabe exactamente adónde ir siguiente. |
| **Aesthetic-Usability** | Pol visual earns trust antes que contenido does. Hermoso feels más fácil de usar.

### Página de Pricing / Subscription

| Principio | Aplicación |
|-----------|------------|
| **Anchoring** | Show premium tier first o most visually prominent. Everything else feels like a deal. |
| **Loss Aversion** | Frame around what free users MISS, not just what paid users get. Losing hurts 2x más. |
| **Default Effect** | Pre-select the recommended tier. Majority users never change defaults. |
| **Commitment/Consistency** | Users who already used free features are primed to subscribe — each step leads to the next. |

### Onboarding / Sign-Up

| Principio | Aplicación |
|-----------|------------|
| **Progressive Commitment** | Small free action first, account second, payment last. |
| **Cognitive Load** | Una pregunta por screen beats un largo form. Remove everything non-essential. |
| **Zeigarnik Effect** | Mostrar progress (step 2 of 4). Incomplete tasks nag — users come back to finish. |
| **Reciprocity** | Dar value antes de asking for info. Free tool access, preview, o sample result. |

### Dashboard / Data Display

| Principio | Aplicación |
|-----------|------------|
| **Chunking** | Group data por categoría o priority — no one giant list. |
| **Spatial Memory** | Layout consistente so returning users find things instantly. No muevas things. |
| **Satisficing** | Highlight the single most important insight. Users pick the first acceptable option. |
| **Recognition Over Recall** | Mostrar full context (labels, timestamps, icons) — no hagan users remember. |

### Checkout / Payment

| Principio | Aplicación |
|-----------|------------|
| **Cognitive Load** | Guest checkout option. Minimal form fields. One decision at a time. |
| **Transparency** | Mostrar TODOS los costs antes del step de payment. Sorpresa fees es la #1 causa de abandono. |
| **Loss Aversion** | Trust badges y guarantees NEXT TO the payment button, not in the footer. |
| **Default Effect** | Pre-select standard shipping. Pre-check "save info." Reduce decisions. |

### About / Trust Page

| Principio | Aplicación |
|-----------|------------|
| **Authority** | Methodology, data sources, team expertise — prove you know what you're doing. |
| **Hierarchy of Trust** | Esta página sirve users at level 2-3 (interest → confidence). No asks for the sale here. |
| **Transparency** | Honest about limitations, not just strengths. Vulnerability builds trust. |

## Fuentes y Fundamentos

1. **Kahneman (Prospect Theory)** — losses hurt ~2x más que gains equivalentes
2. **Norman (Emotional Design)** — beautiful feels easier to use; diseño emocional
3. **Cialdini (Influence)** — principles de persuasión ética
4. **Hick, Fitts, Miller** — principios de memoria y carga cognitiva
5. **Zeigarnik** — efecto: tareas incompletas nag, usuarios vienen a finish
6. **NN/g Psychology for UX study guide** — 112 resources across 11 categories
7. **Anti-patterns éticos** — línea clara entre persuasión y manipulación

## Guía de Implementación Rápida

### Para cada principio aplicable:

1. **¿Qué?** — Definición de principio en 1-2 sentences
2. **¿Cómo?** — Cambio específico en markup, layout o copy
3. **¿El anti-patrón?** — Qué señal de que el principio no se está aplicando (o se está violando)
4. **¿Peso?** — Pesa más que brand, accessibility o technical quality?

### Ejemplo: Anchoring en Pricing Page

**Before** — all tiers equal, no anchor:
```html
<div class="plans">
  <div class="plan">Basic — $19/mo</div>
  <div class="plan">Pro — $49/mo</div>
  <div class="plan">Enterprise — $99/mo</div>
</div>
```

**After** — Pro anchored as the visual default:
```html
<div class="plans">
  <div class="plan">Basic — $19/mo</div>
  <div class="plan featured">        <!-- visualmente prominent, pre-selected -->
    <span class="badge">Most Popular</span>
    Pro — $49/mo
  </div>
  <div class="plan">Enterprise — $99/mo</div>
</div>
```

**Por qué:** El tier destacado se convierte en el anchor. Basic feels like una ganga por comparación. Enterprise existe para hacer Pro se vea razonable. El badge "Most Popular" añade social proof.

## Versión y Mantimiento

- **Versión:** 1.0 (2026)
- **Mantenimiento:** Revisar trimestralmente contra nueva investigación en psicología cognitiva UX
- **Actualizaciones:** Añadir nuevos principios cuando la evidencia sustente su aplicación ética en UX
- **Retiros:** Remover principios que se violen Ética línea entre persuasión y manipulación
## References

[TODO: Add references]
