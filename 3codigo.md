> Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);

> Ao final do processamento, qual será o valor da variável SOMA? 

Reescrevendo o pseudocódigo acima a fim de facilitar sua leitura:

```
int INDICE = 12
int SOMA = 0
int K = 1

enquanto K < INDICE faça {
    K = K + 1;
    SOMA = SOMA + K;
}

imprimir(SOMA);
```

O código será executado até que tenhamos `K = 12`. Neste ponto, a estrutura `enquanto` não é executada, visto que `K` não atende mais à condição do loop (`K < INDICE`).

Para `K = 1` até `K = 11`, `K` será acrescido em 1 e então adicionado à variável `SOMA`. Se analisarmos iteração à iteração, veremos que o valor de `SOMA` ao final será 77, que é finalmente impresso na última linha executada.

**RESPOSTA**: `SOMA = 77`
