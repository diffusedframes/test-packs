"""Check pack file integrity and graph structure only. Never connects to ComfyUI or runs a model."""
import hashlib
import json
import pathlib

root = pathlib.Path(__file__).resolve().parents[1]
pack = root / 'packs/ltx-i2v-01'
manifest = json.loads((pack / 'manifest.json').read_text(encoding='utf-8'))
assert manifest['validation']['gpuRun'] is False, 'Do not claim a GPU run from a file check.'
assert manifest['validation']['referenceEnvironment'] is None
assert manifest['status'] == 'pilot-baseline-pending'
for relative, expected in manifest['files'].items():
    path = (pack / relative).resolve()
    assert path.is_relative_to(pack.resolve()), 'A manifest path escaped the pack.'
    assert hashlib.sha256(path.read_bytes()).hexdigest() == expected, f'Checksum mismatch: {relative}'
graph = json.loads((pack / 'workflow.json').read_text(encoding='utf-8'))
nodes = {node['id']: node for node in graph['nodes']}
links = {link[0]: link for link in graph['links']}
assert len(nodes) == len(graph['nodes']), 'Duplicate root node ID.'
for link in links.values():
    _, origin, origin_slot, target, target_slot, _ = link
    assert origin in nodes and target in nodes, 'Dangling root link.'
    assert nodes[target]['inputs'][target_slot]['link'] == link[0]
    assert link[0] in nodes[origin]['outputs'][origin_slot]['links']
for node in nodes.values():
    for input_item in node.get('inputs', []):
        assert input_item.get('link') is None or input_item['link'] in links
assert 'prompt' not in graph.get('extra', {}), 'Remove stale cached API metadata.'
control = nodes[398]['widgets_values']
assert control[0] == (pack / 'prompt.txt').read_text(encoding='utf-8').strip()
assert control[1:7] == [False, 3, 1280, 736, 41000, 24], 'Preset mismatch.'
assert nodes[395]['widgets_values'][0] == pathlib.Path(manifest['input']['path']).name
assert manifest['preset']['frames'] == control[2] * control[6] + 1
for subgraph in graph['definitions']['subgraphs']:
    subnodes = {node['id']: node for node in subgraph['nodes']}
    for link in subgraph.get('links', []):
        # -10 / -20 are ComfyUI's virtual subgraph input/output nodes.
        assert link['origin_id'] in subnodes or link['origin_id'] in [-10, -20]
        assert link['target_id'] in subnodes or link['target_id'] in [-10, -20]
    assert subnodes[339]['widgets_values'] == [41000, 'fixed']
    assert subnodes[338]['widgets_values'] == [42, 'fixed']
    assert subnodes[383]['widgets_values'] == [False]
print('Pack file hashes and JSON structure checked. No GPU run or performance validation performed.')
