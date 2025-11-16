import numpy as np
import matplotlib.pyplot as plt

class CompressImage():
    def __init__(self):
        self.matrix = None

    def set_image(self, pil_image):
        self.matrix = np.array(pil_image, dtype=float)
        print("Matrix shape:", self.matrix.shape)

    @staticmethod
    def perc_storage(rank, n_rows, n_cols):
        original_space = n_rows * n_cols
        compressed_space = n_rows * rank + rank + n_cols * rank
        return compressed_space / original_space * 100

    @staticmethod
    def perc_energy(S, r):
        return (np.sum(S[:r]) / np.sum(S)) * 100
    

    def svd(self, full_matrices=False):
        U, S_mat, VT = np.linalg.svd(self.matrix, full_matrices=full_matrices)
        return U, np.diag(S_mat), VT
    
    def get_optimal_rank_by_energy(self, S, max_energy):
        max_rank_ = S.shape[0]
        opt_rank_ = 1
        
        while opt_rank_ <= max_rank_:
            energy = self.perc_energy(S, opt_rank_)
            if energy < max_energy:
                opt_rank_ += 1
                continue
            elif energy > max_energy:
                return opt_rank_ - 1
            else:
                return opt_rank_
    
    def get_optimal_rank_by_storage(self, S, max_storage):
        max_rank_ = S.shape[0]
        opt_rank_ = 1
        
        while opt_rank_ <= max_rank_:
            storage = self.perc_storage(opt_rank_, *S.shape)
            if storage < max_storage:
                opt_rank_ += 1
                continue
            if storage > max_storage:
                return opt_rank_ - 1
            else:
                return opt_rank_

    def rank_image(self, MAX_ENERGY=85, MAX_STORAGE=30):
        U, S_mat, V_T = self.svd()
        n_rows, n_cols = self.matrix.shape

        opt_rank_by_energy = self.get_optimal_rank_by_energy(S_mat, MAX_ENERGY) 
        opt_rank_by_storage = self.get_optimal_rank_by_storage(S_mat, MAX_STORAGE) 

        print(f'optimum rank for {MAX_ENERGY}% energy is {opt_rank_by_energy}')
        print(f'optimum rank for {MAX_STORAGE}% storage is {opt_rank_by_storage}')

        RANKS = [5, 25, 50, 100, 200, opt_rank_by_energy, opt_rank_by_storage]
        fig = plt.figure(figsize=(16, 10))

        for idx, r in enumerate(RANKS):
            X_r = U[:, :r] @ S_mat[:r, :r] @ V_T[:r, :]

            ax = plt.subplot(2, 4, idx + 1)
            ax.imshow(X_r, cmap='gray')
            ax.set_xticks([])
            ax.set_yticks([])
            ax.set_title(f'''rank {r}\nspace required: {round(self.perc_storage(r, n_rows, n_cols), 2)}%
            information stored: {round(self.perc_energy(S_mat, r), 2)}''')

        ax = plt.subplot(2, 4, len(RANKS) + 1)
        ax.imshow(self.matrix, cmap='gray')
        ax.set_title("Original")
        ax.set_xticks([])
        ax.set_yticks([])

        plt.tight_layout()
        plt.show()
