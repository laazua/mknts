package org.example.sbapi.entity;

import jakarta.persistence.*;

@Entity
@Table(name = "sb_user")  // 避免使用 user 关键字
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;

    private String email;

    // 无参构造方法
    public User() {
    }

    // 带参构造方法
    public User(String name, String email) {
        this.name = name;
        this.email = email;
    }

    // getter 和 setter 方法
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
}
