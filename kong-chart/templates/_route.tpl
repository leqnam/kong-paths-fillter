{{/*
Define route plugin.
*/}}
{{- define "kong-chart.route" }}
{{- if .Values.routes.plugins }}
- hosts:
  {{- range .Values.routes.hosts }}
    - {{ . }}
  {{- end }}
  https_redirect_status_code: 426
  plugins:
    {{- include "kong-chart.plugins" $ | trim | nindent 2}}
  methods:
  - GET
  - POST
  - PUT
  - DELETE
  - OPTIONS
  - PATCH
  name: {{ .Values.name }}
  tags:
    - {{ .Values.name }}
  paths:
  {{- range .Values.routes.paths }}
    - {{ . }}
  {{- end }}
  strip_path: {{ .Values.routes.strip_path }}
  preserve_host: {{ .Values.routes.preserve_host }}
  protocols:
  - https
tags:
  - {{ .Values.name }}
{{- else}}
- hosts:
  {{- range .Values.routes.hosts }}
    - {{ . }}
  {{- end }}
  https_redirect_status_code: 426
  methods:
  - GET
  - POST
  - PUT
  - DELETE
  - OPTIONS
  - PATCH
  name: {{ .Values.name }}
  tags:
    - {{ .Values.name }}
  paths:
  {{- range .Values.routes.paths }}
    - {{ . }}
  {{- end }}
  strip_path: {{ .Values.routes.strip_path }}
  preserve_host: {{ .Values.routes.preserve_host }}
  protocols:
  - https
tags:
  - {{ .Values.name }}
{{- end }}
{{- end }}