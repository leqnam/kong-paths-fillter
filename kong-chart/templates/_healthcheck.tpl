{{/*
Define upstreams healthcheck.
*/}}
{{- define "kong-chart.upstream" }}
{{- if .Values.upstreams.healthchecks }}
- algorithm: round-robin
  hash_fallback: none
  hash_on: none
  hash_on_cookie_path: /
  healthchecks: 
    active:
      concurrency: 10
      healthy:
        http_statuses:
        - 200
        - 302
        interval: 10
        successes: 1
      http_path: {{ .Values.upstreams.path }}
      https_verify_certificate: true
      timeout: 1
      type: http
      unhealthy:
        http_failures: 3
        http_statuses:
        - 429
        - 404
        - 500
        - 501
        - 502
        - 503
        - 504
        - 505
        interval: 10
        tcp_failures: 3
        timeouts: 5
    passive:
      healthy:
        http_statuses:
        - 200
        - 201
        - 202
        - 203
        - 204
        - 205
        - 206
        - 207
        - 208
        - 226
        - 300
        - 301
        - 302
        - 303
        - 304
        - 305
        - 306
        - 307
        - 308
        successes: 1
      type: http
      unhealthy:
        http_failures: 3
        http_statuses:
        - 429
        - 500
        - 503
        tcp_failures: 3
        timeouts: 5
  name: {{ .Values.name }}
  tags: 
    - {{ .Values.name }}
{{- else}}
- algorithm: round-robin
  hash_fallback: none
  hash_on: none
  hash_on_cookie_path: /
  healthchecks:
    active:
      concurrency: 10
      healthy:
        http_statuses:
        - 200
        - 302
        interval: 10
        successes: 0
      http_path: {{ .Values.upstreams.path }}
      https_verify_certificate: true
      timeout: 1
      type: http
      unhealthy:
        http_failures: 0
        http_statuses:
        - 429
        - 404
        - 500
        - 501
        - 502
        - 503
        - 504
        - 505
        interval: 0
        tcp_failures: 0
        timeouts: 0
    passive:
      healthy:
        http_statuses:
        - 200
        - 201
        - 202
        - 203
        - 204
        - 205
        - 206
        - 207
        - 208
        - 226
        - 300
        - 301
        - 302
        - 303
        - 304
        - 305
        - 306
        - 307
        - 308
        successes: 0
      type: http
      unhealthy:
        http_failures: 0
        http_statuses:
        - 429
        - 500
        - 503
        tcp_failures: 0
        timeouts: 0
  name: {{ .Values.name }}
  tags: 
    - {{ .Values.name }}
{{- end }}
{{- end }}


