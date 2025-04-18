package service

import (
	"errors"
	"fmt"
	"gookins/core"
	"gookins/model"
)

var (
	ErrCreateTask = errors.New("创建任务失败")
	ErrDeleteTask = errors.New("删除任务失败")
	ErrUpdateTask = errors.New("更新任务失败")
	ErrTaskLists  = errors.New("获取任务列表失败")
)

func CreateTask(task model.TaskForm) error {
	fmt.Println(task.Name, task.Description, task.PipeLine)
	dbTask := model.Task{
		Name:        task.Name,
		Description: task.Description,
		PipeLine:    task.PipeLine,
	}
	result := core.Db.Create(&dbTask)
	if result.Error != nil {
		return ErrCreateTask
	}
	return nil
}

func DeleteTask(id uint64) error {
	var task model.Task
	result := core.Db.Where("id = ?", id).Delete(&task)
	if result.Error != nil {
		return ErrDeleteUser
	}
	return nil
}

func UpdateTask(task model.TaskForm) error {
	result := core.Db.Model(&model.Task{}).Where("name = ?", task.Name).Updates(model.Task{Name: task.Name, Description: task.Description, PipeLine: task.PipeLine})
	if result.Error != nil {
		return ErrUpdateTask
	}
	return nil
}

func TaskLists() ([]model.Task, error) {
	var tasks []model.Task
	result := core.Db.Unscoped().Model(&model.Task{}).Select("id, created_at, updated_at, deleted_at, name, description, pipe_line").Find(&tasks)
	if result.Error != nil {
		return nil, ErrTaskLists
	}
	return tasks, nil
}

func TaskDisable(name string, disable bool) error {
	result := core.Db.Model(&model.Task{}).Where("name = ?", name).Update("disabled", disable)
	if result.Error != nil {
		return ErrUpdateTask
	}
	return nil
}
