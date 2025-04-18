package routers

import (
	"msbn/models"
	"msbn/utils"
	"strconv"

	"github.com/gin-gonic/gin"
)

// 用户登录
func Login(c *gin.Context) {
	var userSchema models.UserLoginSchema
	if err := c.BindJSON(&userSchema); err != nil {
		c.JSON(200, gin.H{
			"message": "获取表单参数错误!",
			"data":    nil,
			"code":    400,
		})
		return
	}
	if userSchema.Username == "" || userSchema.Password == "" {
		c.JSON(200, gin.H{
			"message": "用户名或密码不能为空!",
			"data":    nil,
		})
		return
	}
	// 对比数据空的用户名和密码
	if !models.CheckUser(userSchema.Username, userSchema.Password) {
		c.JSON(200, gin.H{
			"message": "用户名或密码错误!",
			"data":    nil,
		})
		return
	}
	// 生成token
	token, err := utils.CreateToken(userSchema.Username)
	if err != nil {
		c.JSON(200, gin.H{
			"message": "生成token错误!",
			"data":    err,
		})
		return
	}
	// 登录成功并返回token
	c.JSON(200, gin.H{
		"message": "登录成功!",
		"token":   token,
		"code":    200,
	})
}

// 用户列表接口
func GetUserList(c *gin.Context) {
	u := models.QuerySysUserList()
	c.JSON(200, gin.H{
		"message": "用户列表接口",
		"data":    u,
		"code":    200,
	})
}

// 获取用户信息
func GetUserInfo(c *gin.Context) {
	username, _ := c.Get("username")
	u, p := models.GetUserByName(username.(string))
	c.JSON(200, gin.H{
		"message": "用户信息",
		"data":    gin.H{"user": u, "permisson": p},
		"code":    200,
	})
}

// 添加用户接口
func AddUser(c *gin.Context) {
	var userSchema models.AddUserSchema
	if err := c.BindJSON(&userSchema); err != nil {
		c.JSON(200, gin.H{
			"message": "获取表单参数错误!",
			"data":    err,
			"code":    400,
		})
		return
	}
	if userSchema.PassOne != userSchema.PassTow {
		c.JSON(200, gin.H{
			"message": "密码不一致!",
			"data":    nil,
			"code":    400,
		})
		return
	}
	if !models.AddSysUser(userSchema.Username, userSchema.PassOne) {
		c.JSON(200, gin.H{
			"message": "创建用户失败!",
			"data":    nil,
			"code":    400,
		})
		return
	}
	c.JSON(200, gin.H{
		"message": "创建用户成功!",
		"data":    userSchema,
		"code":    200,
	})
}

// 更新用户
func UpdateUser(c *gin.Context) {
	var userSchema models.UpUserSchema
	if err := c.BindJSON(&userSchema); err != nil {
		c.JSON(200, gin.H{
			"message": "获取表单参数错误!",
			"data":    err,
			"code":    400,
		})
		return
	}
	if userSchema.PassOne != userSchema.PassTow {
		c.JSON(200, gin.H{
			"message": "密码不一致!",
			"data":    nil,
			"code":    400,
		})
		return
	}
	if !models.UpdateSysUser(userSchema.Username, userSchema.PassOne) {
		c.JSON(200, gin.H{
			"message": "更新失败!",
			"data":    nil,
			"code":    400,
		})
		return
	}
	c.JSON(200, gin.H{
		"message": "更新用户成功!",
		"data":    nil,
		"code":    200,
	})
}

// 删除用户
func DeleteUser(c *gin.Context) {
	var userSchema models.DelUserSchema
	if err := c.BindJSON(&userSchema); err != nil {
		c.JSON(200, gin.H{
			"message": "获取表单参数错误!",
			"data":    nil,
			"code":    400,
		})
		return
	}
	if !models.DeleteSysUser(userSchema.Username) {
		c.JSON(200, gin.H{
			"message": "删除用户失败!",
			"data":    nil,
			"code":    400,
		})
	}
	c.JSON(200, gin.H{
		"message": "删除用户成功!",
		"data":    nil,
		"code":    200,
	})
}

// 根据ID获取单个用户
func GetUserById(c *gin.Context) {
	userid := c.Param("id")
	uid, _ := strconv.ParseUint(userid, 10, 64)
	u := models.GetSysUserById(uid)
	c.JSON(200, gin.H{
		"message": "根据id获取单个用户",
		"data":    u,
	})
}

// 给用户分配角色
func DistributeRoleForUser(c *gin.Context) {
	var urSchema models.UrSchema
	if err := c.BindJSON(&urSchema); err != nil {
		c.JSON(200, gin.H{
			"message": "获取表单参数错误!",
			"data":    err,
			"code":    400,
		})
		return
	}
	if !models.UserAndRole(urSchema.Username, urSchema.Rolename) {
		c.JSON(200, gin.H{
			"message": "给用户分配角色失败!",
			"data":    nil,
			"code":    400,
		})
		return
	}
	c.JSON(200, gin.H{
		"message": "给用户分配角色成功!",
		"data":    nil,
		"code":    200,
	})
}
