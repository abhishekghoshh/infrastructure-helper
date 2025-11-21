# Introduction

GitLab CI/CD is a powerful continuous integration and continuous deployment tool built into GitLab. It allows you to automatically build, test, and deploy your code whenever changes are made to your repository. The CI/CD pipeline is defined using a YAML configuration file that describes the various stages and jobs that should be executed.

## Sample `.gitlab-ci.yml`

Below is a basic GitLab CI pipeline configuration that demonstrates a simple build and test workflow:

```yaml
stages:
    - build
    - test

create_file:
    image: alpine
    stage: build
    script:
        - echo "Building ...."
        - mkdir build
        - touch build/reports.txt
    artifacts:
        paths:
            - build/

test_file:
    image: alpine
    stage: test
    script:
        - test -f build/reports.txt
```

### Explanation

This example pipeline demonstrates several key GitLab CI/CD concepts:

- **stages**: Defines the pipeline stages that run sequentially. Stages allow you to organize jobs logically and control the order of execution. All jobs within the same stage run in parallel, while stages execute one after another.

- **create_file job**: 
    - Uses the lightweight Alpine Linux Docker image as the runtime environment
    - Executes during the build stage
    - Creates a build directory and generates a reports file to simulate a build process
    - Stores the build directory as an artifact using the `artifacts` keyword (note: fixed typo from `artifcats` to `artifacts`)
    - Artifacts are files or directories that are saved after a job completes and can be used by subsequent jobs or downloaded

- **test_file job**:
    - Runs in the test stage after the build stage completes successfully
    - Verifies that the reports file was created by the previous job
    - Automatically has access to artifacts from previous stages without additional configuration
    - Uses the `test` command to check file existence, which will fail the job if the file is not found

### Key Concepts Illustrated

1. **Pipeline Flow**: The pipeline follows a logical sequence: build → test
2. **Artifact Sharing**: Build outputs are automatically available to subsequent stages
3. **Job Dependencies**: The test job implicitly depends on the successful completion of the build job
4. **Docker Integration**: Each job runs in an isolated Docker container
5. **Script Execution**: Jobs can execute multiple shell commands in sequence

**Important Notes**: 
- The configuration file must be named `.gitlab-ci.yml` (not `.gitlab-ci.yaml`) and placed in the root directory of your repository
- Each job runs in a fresh environment, making artifacts essential for sharing data between jobs
- If any job in a stage fails, subsequent stages will not execute by default