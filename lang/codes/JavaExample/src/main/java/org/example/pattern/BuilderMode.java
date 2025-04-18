package org.example.pattern;

/**
 * builder模式
 */
public class BuilderMode
{
    private int x;
    private int y;
    private String name;

    private BuilderMode(Builder builder) {
        this.x = builder.x;
        this.y = builder.y;
        this.name = builder.name;
    }

    public static class Builder {
        private int x;
        private int y;
        private String name;

        public Builder setX(int x) {
            this.x = x;
            return this;
        }

        public Builder setY(int y) {
            this.y = y;
            return this;
        }

        public Builder setName(String name) {
            this.name = name;
            return this;
        }

        public BuilderMode build() {
            return new BuilderMode(this);
        }
    }

    public void printValues() {
        System.out.printf("x: %d, y: %d, name: %s\n", x, y, name);
    }
}
