import copy, importlib.util, json, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
SPEC=importlib.util.spec_from_file_location('runner_validator',ROOT/'validators/validate_private_runner_framework.py')
MOD=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(MOD)

class PrivateRunnerFrameworkTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.positive=json.loads((ROOT/'fixtures/private-runner/positive-lingxi-shaped.json').read_text())
        cls.cases=json.loads((ROOT/'fixtures/private-runner/negative-cases.json').read_text())
    def test_positive(self): self.assertIsNone(MOD.validate_bundle(self.positive))
    def test_negative_matrix(self):
        for case in self.cases:
            with self.subTest(case=case['name']):
                sample=copy.deepcopy(self.positive); MOD.set_path(sample,case['path'],case['value'])
                self.assertEqual(MOD.validate_bundle(sample),case['expected_blocker'])
    def test_public_framework_never_registers_runner(self):
        text=(ROOT/'starter-kit/private-runner/README.md').read_text()
        self.assertIn('does not register',text.lower())
        self.assertIn('consumer private repository',text.lower())
if __name__=='__main__': unittest.main()
