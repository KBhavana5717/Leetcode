class Solution {
    private int maxSum = Integer.MIN_VALUE;

    public int maxPathSum(TreeNode root) {
        dfs(root);
        return maxSum;
    }

    private int dfs(TreeNode node) {
        if (node == null) return 0;

        int leftGain = Math.max(dfs(node.left), 0);
        int rightGain = Math.max(dfs(node.right), 0);

        int currPath = node.val + leftGain + rightGain;
        maxSum = Math.max(maxSum, currPath);

        return node.val + Math.max(leftGain, rightGain);
    }
}
