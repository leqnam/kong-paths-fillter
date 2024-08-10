{{/*
Define route plugin.
*/}}
{{- define "kong-chart.plugins" }}
{{- range $key, $values := .Values.routes.plugins -}}
{{- if eq $values "cors" }}
- config:
    credentials: false
    headers:
    - '*'
    max_age: 3600
    methods:
    - PUT
    - GET
    - POST
    - DELETE
    - OPTIONS
    origins:
    - '*'
    preflight_continue: false
  enabled: true
  name: cors
{{- end }}
{{- if eq $values "jwt" }}
- config:
    anonymous: null
    claims_to_verify:
    - exp
    cookie_names: []
    header_names:
    - authorization
    key_claim_name: iss
    maximum_expiration: 0
    run_on_preflight: true
    secret_is_base64: false
    uri_param_names:
    - jwt
  enabled: true
  name: jwt
{{- end }}
{{- end }}
{{- end }}