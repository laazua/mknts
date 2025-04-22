package parser

type Inventory struct {
	Addr      string         `mapstructure:"addr"`
	Port      string         `mapstructure:"port"`
	User      string         `mapstructure:"user"`
	Password  string         `mapstructure:"password"`
	ExtraVars map[string]any `mapstructure:"extraVars"`
}
