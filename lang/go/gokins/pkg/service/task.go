package service

import (
	"fmt"
	"log/slog"
	"os"
	"os/exec"

	"gokins/pkg/model"

	"gopkg.in/yaml.v2"
)

func ParseTask(fileName string) error {
	content, err := os.ReadFile(fileName)
	if err != nil {
		slog.Error(fmt.Sprintf("## 任务文件不存在: %v\n", err))
		return err
	}

	var taskTpl model.TaskTemplate

	if err = yaml.Unmarshal(content, &taskTpl); err != nil {
		return err
	}

	fmt.Printf("Run task: %v\n", taskTpl.Task.Name)
	for _, step := range taskTpl.Task.Steps {
		fmt.Printf("Run step: %v\n", step.Name)
		RunCommand(step.Cmd)
	}

	return nil
}

func RunCommand(cmd string) {
	out, err := exec.Command("bash", "-c", cmd).Output()
	if err != nil {
		panic(err)
	}
	fmt.Printf("Command: %v\n", string(out))
}
