package config

type Reader struct{}

func (r *Reader) CA() CAView {
	return CAView{cfg: cfg}
}

func (r *Reader) Bastion() BastionView {
	return BastionView{cfg: cfg}
}

func (r *Reader) Err() error {
	return err
}
