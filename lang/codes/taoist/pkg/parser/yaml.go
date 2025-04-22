package parser

import (
	"fmt"

	m "taoist/pkg/modules"

	"gopkg.in/yaml.v3"
)

func ParseModule(module map[string]interface{}) (m.Module, error) {
	if cmd, exists := module["command"]; exists {
		command := &m.Command{}
		data, err := yaml.Marshal(cmd)
		if err != nil {
			return nil, err
		}
		if err := yaml.Unmarshal(data, command); err != nil {
			return nil, err
		}
		return command, nil
	}

	if cp, exists := module["copy"]; exists {
		copy := &m.Copy{}
		data, err := yaml.Marshal(cp)
		if err != nil {
			return nil, err
		}
		if err := yaml.Unmarshal(data, copy); err != nil {
			return nil, err
		}
		return copy, nil
	}

	return nil, fmt.Errorf("unknown module type")
}
