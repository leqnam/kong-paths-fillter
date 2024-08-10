{{/*
Define targets of upstream.
*/}}
{{- define "kong-chart.targetsUpstream" }}
{{- if eq .Values.env "UAT" }}
- target: 10.56.239.141:{{ .Values.upstreams.port }}
- target: 10.56.239.142:{{ .Values.upstreams.port }}
- target: 10.56.239.143:{{ .Values.upstreams.port }}
{{- end }}
{{- if eq .Values.env "DEV" }}
- target: 10.56.239.103:{{ .Values.upstreams.port }}
- target: 10.56.239.104:{{ .Values.upstreams.port }}
- target: 10.56.239.105:{{ .Values.upstreams.port }}
- target: 10.56.239.106:{{ .Values.upstreams.port }}
- target: 10.56.239.107:{{ .Values.upstreams.port }}
{{- end }}
{{- if eq .Values.env "DEV2" }}
- target: 10.26.137.136:{{ .Values.upstreams.port }}
- target: 10.26.137.137:{{ .Values.upstreams.port }}
- target: 10.26.137.138:{{ .Values.upstreams.port }}
- target: 10.26.137.139:{{ .Values.upstreams.port }}
- target: 10.26.137.140:{{ .Values.upstreams.port }}
{{- end }}
{{- end }}