
dataset_config = {
    'source_train': 'data/train/source',
    'target_train': 'data/train/target',
    'source_valid': 'data/valid/source',
    'target_valid': 'data/valid/target',
    'source_vocab': 'vocab/source',
    'target_vocab': 'vocab/target',
}

model_config = {
    'cell_type': 'lstm',
    'attention_type': 'bahdanau', #luong
    'hidden_units': 512,
    'enc_depth': 2,
    'dec_depth': 2,
    'embedding_size': 500,
    'num_encoder_symbols': 30000,
    'num_decoder_symbols': 30000,
    'use_residual': True,
    'use_dropout': True,
    'dropout_rate': 0.3,
    'attn_input_feeding': False, # Use input feeding method in attentional decoder
}
train_config = {
    'learning_rate' : 0.0002,
    'max_gradient_norm': 1.0,
    'batch_size' : 128,
    'max_epochs': 10,
    'max_load_batches': 20,
    'max_seq_length': 50,
    'display_freq': 100,
    'save_freq': 1150000,
    'optimizer': 'adam',
    'model_dir': 'model/'
    'model_name': 'seq2seq.ckpt',
    'shuffle_each_epoch': True,
    'sort_by_length': True,
    'use_f16': False,
}