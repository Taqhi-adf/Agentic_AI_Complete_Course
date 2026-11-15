#  Level 14 – Testing, monitoring and deployment

# Learn these tools:

# | Technology     | What to practice             |
# | -------------- | ---------------------------- |
# | Pytest         | Automated agent tests        |
# | LangSmith      | Agent traces and evaluations |
# | Langfuse       | Observability                |
# | MLflow         | Experiment tracking          |
# | Prometheus     | Metrics                      |
# | Docker         | Containerization             |
# | GitHub Actions | CI/CD                        |
# | PostgreSQL     | Persistent state             |
# | Redis          | Caching                      |
# | AWS EC2        | Deployment                   |
# | Azure          | Cloud deployment             |

### Code 36: Agent testing using pytest

# Install: pip install pytest

# Create `15_deployment/test_agent.py`.


def add(a, b):
    return a + b


def test_addition():
    assert add(10, 20) == 30

    def test_zero():
        assert add(0, 0) == 0

        def test_negative():
            assert add(-5, 5) == 0


# Run: pytest -v
