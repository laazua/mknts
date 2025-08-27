package api

import (
	"net/http"
	"strconv"

	"layershow/internal/dto"
	"layershow/internal/service"
	"layershow/pkg/core"
)

type UserHandler struct {
	service *service.UserService
}

func NewUserHandler(s *service.UserService) *UserHandler {
	return &UserHandler{service: s}
}

func (h *UserHandler) RegisterRoutes(route *core.Router) {
	route.Post("/users", h.CreateUser)
	route.Get("/users/:id", h.GetUser)
}

func (h *UserHandler) CreateUser(w http.ResponseWriter, r *http.Request) {
	var req dto.UserCreateRequest
	if err := core.Bind(r, &req); err != nil {
		core.Failure(w, core.Map{"error": err.Error()})
		return
	}

	resp, err := h.service.CreateUser(&req)
	if err != nil {
		core.Failure(w, core.Map{"error": err.Error()})
		return
	}
	core.Success(w, core.Map{"code": 200, "data": resp})
}

func (h *UserHandler) GetUser(w http.ResponseWriter, r *http.Request) {
	id, err := strconv.Atoi(core.Param(r, "id"))
	if err != nil {
		core.Failure(w, core.Map{"code": 400, "message": err.Error()})
		return
	}

	resp, err := h.service.GetUser(id)
	if err != nil {
		core.Failure(w, core.Map{"code": 400, "message": err.Error()})
		return
	}
	core.Success(w, core.Map{"code": 200, "data": resp})
}
