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

---

## Categorías de Principios (11 categorias — total: 65 principios)

| Categoría | Count | Core Insight |
|----------|-------|--------------|
| Attention | 4 | Users see less than you think |
| Gestalt | 8 | Visual grouping drives comprehension |
| Memory | 10 | Recognition beats recall; chunk everything |
| Sensemaking | 3 | Mental models shape expectations |
| Decision Making | 5 | Fewer choices, clearer outcomes |
| Motor/Interaction | 3 | Big targets, fast responses |
| Motivation | 4 | Autonomy + competence + relatedness |
| Cognitive Biases | 10 | Defaults persist; first impressions anchor |
| Persuasion | 9 | Trust before ask; prove before promise |
| Emotion | 6 | Beautiful feels easier; delight earns loyalty |
| Ethics | 3 | Bright line between persuasion and manipulation |

### Búsqueda Rápil por Principio

Cada principio tiene:
- **Definición concisa** — qué significa en contexto UX
- **Aplicación prática** — qué hacer en diseño
- **Anti-patrón** — qué evitar
- **Implicaciones de diseño** — qué cambiar en markup, layout o copy

### Peso de Principios en Decisiones de Diseño

1. **Brand identity** — El diseño debe resonar con los valores y personalidad de la marca
2. **Accesibilidad** — WCAG compliance es no negociable; contraste de color mínimo, targets táctiles tamaño
3. **Performance** — Diseño responsive, loading times aceptables, recursos optimizados
4. **Principios UX** — Influencia sutil en decisiones de layout, copy y jerarquía visual

### Anti-Patrones (Nunca Hagas)

- **Fake scarcity counters** — si no es real, no lo muestre
- **Confirmshaming** — "No, I don't want to save money" es manipulativo
- **Hidden costs at checkout** — la #1 causa de carrito abandonment
- **Forced continuity** — suscripciones difficult-to-cancel erosion all trust
- **Misdirection** — tricks visuales para forzar clicks equivocados
- **Fake social proof** — testimonios fabricados o números inflados
- **Dark defaults** — pre-checking opt-ins que el usuario no pidió
- **Roach motel patterns** — fácil entrar, impossible salir

---

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

---

## Plantilla de Revisión de Diseño

Al revisar un diseño, pregunta:

1. ¿Qué principios UX psicológicos estoy aplicando intencionalmente?
2. ¿Cuáles me estoy perdiendo para el tipo de página o componente?
3. ¿Algún anti-patrón está violando sin darme cuenta?
4. ¿Pesa cada principio contra brand, accessibility y technical quality en la jerarquía correcta?
5. ¿Qué cambio específico y implementable recomiendo?

---

## Versión y Mantimiento

- **Versión:** 1.0 (2026)
- **Mantenimiento:** Revisar trimestralmente contra nueva investigación en psicología cognitiva UX
- **Actualizaciones:** Añadir nuevos principios cuando la evidencia sustente su aplicación ética en UX
- **Retiros:** Remover principios que se violen Ética línea entre persuasión y manipulación
## References

[TODO: Add references]
