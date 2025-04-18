package org.example.sbapi.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.example.sbapi.entity.User;

public interface UserRepository extends JpaRepository<User, Long> {
    // JpaRepository 已经包含了常用的增删改查方法
}
