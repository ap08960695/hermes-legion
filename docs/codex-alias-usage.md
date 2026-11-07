# Official Codex aliases and usage accounting

An existing named custom provider can point to the official Codex endpoint.
Previously, usage accounting classified that alias as an unknown custom billing
route. A cold pricing lookup could then probe both `/models` and `/v1/models`
after a successful response. A constrained worker could finish its first model
request and then be stopped by those unnecessary catalog reads.

v0.8.28 recognizes the official route using the same HTTPS, host, port and path
helper as the native transport. It uses the existing subscription-included cost
entry without a catalog lookup. Input, output and cache tokens remain recorded;
the included cost label retains its existing note about subscription usage.
It does not represent a separate API invoice or a reduction in model requests.

Custom proxies, HTTP, alternate ports and unrelated paths do not inherit this
classification. Models, credentials, quotas, fallback settings and saved work
are preserved.

## Verification

Five accepted-route regressions failed before the fix. The connected native
selection passes **109 tests in nine files**. The installed Linux and Mac
interpreters each pass five positive and eight negative routing controls, with
zero catalog attempts. The offline response/accounting/response integration
also retains both complete mock bodies without poisoning later admission.

The complete **976-path** source kit passes reverse, exact base hashes, forward
application and exact installed hashes. Both installed hosts pass the full
compatibility check. Their production Gateways stay closed; configuration,
account and saved-work checks pass. No new Desktop build or UI acceptance is
claimed for this backend change.

## Bounded live cards

The authorized batch created **eight fresh simple cards** and used **13 physical
model requests**, within its 32-request cap. Six cards completed the same short
arithmetic result with two requests each, full response-body consumption,
canonical session usage and observed managed-client termination. Their native
cost status and billing mode are subscription-included. Every private Gateway
was stopped, and the 1,132 protected production paths remained unchanged.

Two earlier cards remain failures and were never replayed. The first exposed a
private test guard parsing a compressed request as plain JSON and made zero
physical requests. The second made one complete model request before exposing
the pricing-catalog issue. Their evidence and usage remain in the total.

Two profile-matched comparison pairs ran in opposite layout orders:

| Layout | Cards | Full input tokens | Cached input tokens | Cache read | Median dispatch to observed client exit |
| --- | ---: | ---: | ---: | ---: | ---: |
| 3 | 2 | 42,557 | 19,968 | 46.92% | 11.29 s |
| 4 | 2 | 42,555 | 19,968 | 46.92% | 10.31 s |

Both pairs returned the same result and 73 output tokens per card. Layout 4
preserved equal common prefixes and routing keys across the two profile hints;
layout 3 retained different prefixes and keys. This did **not establish a cache
hit improvement**. Two further baseline cards are separate observations, one
with no cache read; using their unequal sample count to claim layout savings
would be misleading.

The small trial was not randomized and did not control provider cache retention
or routing. Client exit used 0.5-second polling. The timing difference is an
observation, not a causal or general speed claim. No Linux GPU was exposed.
