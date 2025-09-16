## Mindstix Bootcamp 2025

[![Infrastructure](https://github.com/rhlm-msx/bootcamp/actions/workflows/infra.yaml/badge.svg)](https://github.com/rhlm-msx/bootcamp/actions/workflows/infra.yaml)

- [x] Setup Github Workflow (with the help of github market place).
- [ ] Github Pages.


Changing Approach
1. Github Pages: Host Webapp
2. AWS Infrasture: Hosts RESTapi and rest of the resources.

```mermaid

flowchart LR

push[Push]
step1(Create Infra on AWS)
step2(Replace Correct Lambda FURL in Static pages)
step3(Publish site to github pages)

push --> step1
push --> step2
push --> step3

```


Todo
1. Get Site Working
    - Front End Working with proper reporting of error and have correct remote(dns) for backend instance.



## Resources and References

- [Terraform Remote Backend](https://stackoverflow.com/questions/47913041/initial-setup-of-terraform-backend-using-terraform)
