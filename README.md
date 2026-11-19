# Diagnóstico Tributario Pyme

Aplicativo de diagnóstico tributario para micro y pequeñas empresas peruanas: cruce de SIRE con lo declarado, alertas del buzón SOL, deudas y un informe automático.

Estado: fase 0 (repositorio y entorno). Ver el documento de estructura funcional para el alcance de cada fase.

## Reglas de seguridad
- Nunca subir claves SOL, client_id/client_secret, llaves de pasarela ni datos de contribuyentes reales.
- Las credenciales van en Secret Manager (Google Cloud), no en el código ni en archivos.
